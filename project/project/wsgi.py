import os
from django.cor.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project.settings')
application=get_wsgi_application()