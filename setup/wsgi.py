import os
from django.core.wsgi import get_wsgi_application

# 1. Substitua 'NOME_DO_SEU_PROJETO' pelo nome da pasta onde está o seu settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NOME_DO_SEU_PROJETO.settings')

application = get_wsgi_application()

# 2. Esta linha é obrigatória para a Vercel encontrar o projeto
app = application
