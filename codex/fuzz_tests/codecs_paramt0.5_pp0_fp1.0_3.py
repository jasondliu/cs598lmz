import codecs
codecs.register_error("strict", codecs.ignore_errors)

import os
import re
import sys
import time
import gzip
import cStringIO
import errno
import mimetypes
import logging
import traceback
import urllib
import urlparse
import BaseHTTPServer
import cgi
import subprocess
import threading
import SocketServer

from wsgiref.handlers import SimpleHandler
from wsgiref.util import FileWrapper
from wsgiref.headers import Headers

from django.core.handlers.wsgi import STATUS_CODE_TEXT
from django.core.servers.basehttp import WSGIRequestHandler, WSGIServer, \
    WSGIServerException, ServerHandler, get_internal_wsgi_application, \
    DEFAULT_WSGI_ALIAS
from django.core.management.color import color_style
from django.core.management.commands.runserver import naiveip_re
from django.utils import translation
from django.utils.encoding import force_unicode
from django.utils.importlib
