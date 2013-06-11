import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'django_multihost.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

path = '/app'
if path not in sys.path:  sys.path.append(path)
