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
