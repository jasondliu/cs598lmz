import socket
import sys
import threading
import time
import traceback
import urllib
import urllib2
import urlparse

from lxml import etree

from django.conf import settings
from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseServerError
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from django.utils.translation import ugettext as _

from django_openid.auth import OpenIDBackend
from django_openid.models import UserOpenidAssociation
from django_openid.store import DjangoOpenIDStore

from openid.consumer.consumer import Consumer, SUCCESS, CANCEL, FAILURE, SETUP_NEEDED
from openid.consumer.discover import DiscoveryFailure
from openid.extensions import sreg
from openid.fetchers import HTTPFetch
