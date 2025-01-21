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

