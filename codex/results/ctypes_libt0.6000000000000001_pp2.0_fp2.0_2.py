import ctypes
ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Users\\SANTOSH\\Desktop\\new.jpg" , 0)

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
