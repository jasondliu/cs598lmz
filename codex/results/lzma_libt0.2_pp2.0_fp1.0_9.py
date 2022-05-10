import lzma
lzma.LZMAError

import os
os.environ['PYTHON_EGG_CACHE'] = '/tmp'

import sys
sys.path.append('/home/ec2-user/src/')

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
