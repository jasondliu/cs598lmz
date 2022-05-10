import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from pytimeparser   import parse as tp_parse
from .models import *
from .mixins import *
from .templates import *
from .local_settings import *
from .exceptions import *
from .functions import *
from .cron import *
from .themes import get_theme

from operator import itemgetter
from django.core import serializers
#from django.core.serializers import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core.context_processors import csrf
from django.contrib.gis.geos import *
import json
from datetime import datetime, date
import re
from requests import post
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cs
