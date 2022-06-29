import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blango.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "Prod")

from configurations.wsgi import get_wsgi_application

application = get_wsgi_application()