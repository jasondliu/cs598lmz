import types
types.ModuleType

from django.conf import settings
DEBUG = socket.gethostname() == settings.INTERNAL_IPS[0]
if settings.DEBUG is True:
    DEBUG = True
from django.conf import settings
from django.template import TemplateSyntaxError, Node, Variable
from django.template.loader import render_to_string, get_template
from django.template import Context, Template, Library
