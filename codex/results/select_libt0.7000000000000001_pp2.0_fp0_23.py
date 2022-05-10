import select
import socket
import sys
import threading
import time
import traceback
# import urllib.request
import urllib2

from . import httpmessage, loggingconfig
from . import logger
from . import proxyserver
from . import sqlitecache

# The following constants are used to identify the type of request.
REQUEST_CONNECT = 1
REQUEST_GET = 2
REQUEST_HEAD = 3
REQUEST_POST = 4
REQUEST_PUT = 5
REQUEST_DELETE = 6
REQUEST_PATCH = 7
REQUEST_TRACE = 8
REQUEST_OPTIONS = 9
REQUEST_UNKNOWN = 10

# The following constants are used to identify the type of response.
RESPONSE_OK = 200
RESPONSE_CREATED = 201
RESPONSE_ACCEPTED = 202
RESPONSE_NO_CONTENT = 204
RESPONSE_MULTIPLE_CHOICES = 300
RESPONSE_MOVED_PERMANENTLY = 301
RESPONSE_FOUND = 302
RESPON
