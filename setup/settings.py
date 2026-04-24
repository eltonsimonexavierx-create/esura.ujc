import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SEGURANÇA: Mantém a tua SECRET_KEY aqui
SECRET_KEY = 'django-insecure-teu-codigo-aqui'

DEBUG = True # Muda para False quando o design estiver 100% pronto

ALLOWED_HOSTS = ['*'] # Permite que a Vercel aceda ao site

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portal', # A tua aplicação
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # ESSENCIAL PARA O LOGO NA VERCEL
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'setup.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'setup.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --- CONFIGURAÇÃO DE FICHEIROS ESTÁTICOS (A SOLUÇÃO DO LOGO) ---

STATIC_URL = '/static/'

# Pasta onde guardas as imagens no VS Code
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Pasta onde a Vercel vai recolher tudo para o link final
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Ativa a compressão e cache do WhiteNoise (faz o site carregar o design certo)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

