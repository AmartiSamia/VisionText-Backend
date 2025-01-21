to run backend django you need a front end react for this app and you must install the requirement.txt
and also torch here is some pip commands that may help 


python -m venv myenv
myenv\Scripts\activate
python manage.py createsuperuser 
python manage.py makemigrations 
python manage.py migrate
python manage.py startapp authentication
python manage.py startapp generateImage
pip install django djangorestframework
pip install djangorestframework-simplejwt
pip install django-cors-headers
python -m ensurepip
python -m pip install setuptools wheel
python -m pip install --upgrade pip 
pip install -r requirements.txt
pip install torch diffusers pillow
pip install customtkinter Pillow diffusers transformers
pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu118
pip3 install torch torchvision torchaudio
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install accelerate
###############################
certifi==2022.9.14
charset-normalizer==2.1.1
colorama==0.4.5
customtkinter==4.6.1
darkdetect==0.7.1
diffusers==0.3.0
filelock==3.8.0
huggingface-hub==0.9.1
idna==3.4
importlib-metadata==4.12.0
numpy==1.23.3
packaging==21.3
Pillow==9.2.0
pyparsing==3.0.9
PyYAML==6.0
regex==2022.9.13
requests==2.28.1
tk==0.1.0
tokenizers==0.12.1
torch==1.12.1+cu113
torchaudio==0.12.1+cu113
torchvision==0.13.1+cu113
tqdm==4.64.1
transformers==4.22.1
typing_extensions==4.3.0
urllib3==1.26.12
zipp==3.8.1
