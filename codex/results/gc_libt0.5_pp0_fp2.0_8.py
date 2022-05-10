import gc, weakref

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.template.loader import render_to_string

from django_xhtml2pdf.utils import generate_pdf

from ajax_select import make_ajax_field
from ajax_select.fields import AutoCompleteSelectMultipleField
from ajax_select.forms import AutoCompleteSelectWidget
from ajax_select.helpers import make_html_options, make_hidden_input
from ajax_select.registry import registry

from
