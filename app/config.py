import os
from datetime import timedelta

APP_NAME = "Project_Flask"

# Pasta raiz do projeto
ROOT_PATH = ""

# Retorna o caminho absoluto do diretório do arquivo atual
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# Habilita o modo debug
DEBUG = True

# Diretórios de upload
UPLOAD_FOLDER = os.path.join(BASEDIR, "app/static/uploads")
UPLOAD_FOLDER_PHOTO = os.path.join(BASEDIR, "app/static/uploads/images/photo")
