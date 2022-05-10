import weakref
import logging

from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils import simplejson
from django.utils.translation import ugettext as _

from desktop.lib.django_util import render
from desktop.lib.django_util import login_notrequired
from desktop.lib.django_util import JsonResponse
from desktop.lib.django_util import PopupException
from desktop.lib.django_util import format_preserving_redirect
from desktop.lib.exceptions_renderable import PopupException as PopupExceptionRenderable
from desktop.lib.exceptions import StructuredException
from desktop.lib.i18n import smart_str
from desktop.lib.rest.http_client import RestException
from desktop.models import Document
from desktop.models import Document2
from desktop.models import Document2Permission

