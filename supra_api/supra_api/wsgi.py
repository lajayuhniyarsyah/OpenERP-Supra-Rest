"""
WSGI config for Django_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "supra_api.settings")

application = get_wsgi_application()
sys.path.append('/home/adit/restDjango/OpenERP-Supra-Rest')
sys.path.append('/home/adit/restDjango/OpenERP-Supra-Rest/supra_api')
sys.path.append('/home/adit/restDjango/OpenERP-Supra-Rest/supra_api/supra_api')
