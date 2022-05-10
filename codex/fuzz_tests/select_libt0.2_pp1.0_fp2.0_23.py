import select
import socket
import sys
import threading
import time
import traceback
import urllib
import urllib2
import urlparse
import xml.dom.minidom

from xml.parsers.expat import ExpatError

from django.conf import settings
from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.utils.encoding import smart_str

from django_openid.models import UserOpenidAssociation
from django_openid.signals import openid_login_complete
from django_openid.store import DjangoOpenIDStore
from django_openid.util import OpenID, DiscoveryFailure, DjangoOpenIDException
from django_openid.util import from_openid_response, to_openid_request
from django_openid.util import OpenID as OpenIDConsumer

from openid.consumer.consumer import Consumer, \
    SUCCESS, CANCEL, FAILURE, SETUP_NEEDED
from openid.consumer.discover import DiscoveryFailure
from open
