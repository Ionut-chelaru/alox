# filepath: c:\Users\angac\OneDrive\Desktop\alox_vm\Backend\alox\wsgi.py
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alox.settings')

application = get_wsgi_application()