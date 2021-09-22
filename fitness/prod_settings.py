import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get("DEBUG", default=0))

ALLOWED_HOSTS = ['*']
# Настройка почты

DATABASES = {

    'default': {
        "ENGINE": 'django.db.backends.postgresql_psycopg2',
        "NAME": 'fitness_bd',
        "USER": 'fitness',
        "PASSWORD": 'PWghdRet',
        "HOST": 'localhost',
        "PORT": '5432',
    }

}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
