import torch
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from PIL import Image
from diffusers import StableDiffusionPipeline
from django.http import FileResponse
import os
import tempfile

# Auth token for HuggingFace
# Utiliser la variable d'environnement pour sécuriser le token
auth_token = os.getenv("HF_AUTH_TOKEN")

modelid = "CompVis/stable-diffusion-v1-4"
device = "cuda" if torch.cuda.is_available() else "cpu"
dtype = torch.float16 if device == "cuda" else torch.float32

# Charger le pipeline au démarrage du serveur
pipe = StableDiffusionPipeline.from_pretrained(
    modelid,
    revision="fp16",
    torch_dtype=dtype,
    use_auth_token=auth_token
)
pipe.to(device)

class GenerateImageView(APIView):
    parser_classes = [JSONParser]

    def post(self, request):
        prompt = request.data.get("prompt")
        if not prompt:
            return Response({"error": "Prompt is required"}, status=400)

        try:
            # Générer l'image
            if device == "cuda":
                with torch.autocast("cuda"):
                    image = pipe(prompt, guidance_scale=8.5).images[0]
            else:
                image = pipe(prompt, guidance_scale=8.5).images[0]

            # Sauvegarder l'image dans un fichier temporaire
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
            image.save(temp_file.name)

            # Retourner l'image sous forme de fichier
            return FileResponse(
                open(temp_file.name, "rb"),
                as_attachment=True,
                filename="generated_image.png"
            )
        except Exception as e:
            return Response({"error": str(e)}, status=500)
