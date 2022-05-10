import codecs
# Test codecs.register_error('strict', codecs.ignore_errors)
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

from base.models import *
from base.forms import *
from base.decorators import *
from base.utils import *
from base import const

