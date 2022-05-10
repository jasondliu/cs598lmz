import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

import time
import requests

from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseForbidden
from django.http import HttpResponseNotFound

from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_GET


from models import *
from utils import *
from copy import copy
from requests.exceptions import RequestException


from IPython import embed


@require_http_methods(["GET"])
def rate(request):
    term = request.GET.get('term')
    ratio = request.GET.get('ratio')
    compact = request.GET.get('compact')
    from_currencies = request.GET.getlist('from')
    to_currencies = request.
