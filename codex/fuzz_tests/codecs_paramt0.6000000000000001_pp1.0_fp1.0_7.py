import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Local imports
from . import constants
from . import utils
from . import template

# Django imports
from django.http import HttpResponse
from django.conf import settings
from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse
from django.core.exceptions import ImproperlyConfigured
from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site

# Python imports
import os
import re
import unicodedata
import urllib
import urllib2
import logging

# Google imports
from apiclient import errors
from apiclient.http import MediaFileUpload
from apiclient.discovery import build

# Logger
logger = logging.getLogger(__name__)

# Globals
# TODO: Should be in settings.py
SERVICE_ACCOUNT_EMAIL = "679841474961-jn0b7kkk8b1t1
