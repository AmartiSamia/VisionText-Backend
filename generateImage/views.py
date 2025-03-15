import torch
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from PIL import Image
from diffusers import StableDiffusionPipeline
from django.http import FileResponse
import os

# Auth token for HuggingFace
from authtoken import auth_token # Remplacez par votre fichier contenant `auth_token`

modelid = "CompVis/stable-diffusion-v1-4"
device = "cuda" if torch.cuda.is_available() else "cpu"
dtype = torch.float16 if device == "cuda" else torch.float32

# Load the pipeline once when the server starts
pipe = StableDiffusionPipeline.from_pretrained(
    modelid,
    revision="fp16",
    torch_dtype=dtype,
    # use_auth_token=auth_token
)
pipe.to(device)

class GenerateImageView(APIView):
    parser_classes = [JSONParser]

    def post(self, request):
        prompt = request.data.get("prompt")
        if not prompt:
            return Response({"error": "Prompt is required"}, status=400)

        try:
            if device == "cuda":
                with torch.autocast("cuda"):
                    image = pipe(prompt, guidance_scale=8.5).images[0]
            else:
                image = pipe(prompt, guidance_scale=8.5).images[0]

            image_path = "generated_image.png"
            image.save(image_path)
            return FileResponse(
                open(image_path, "rb"), as_attachment=True, filename="generated_image.png"
            )
        except Exception as e:
            return Response({"error": str(e)}, status=500)