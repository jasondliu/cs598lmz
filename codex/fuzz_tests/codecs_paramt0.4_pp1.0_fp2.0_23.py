import codecs
codecs.register_error('strict', codecs.ignore_errors)

import sys
import os
import re
import time
import logging
import logging.handlers
import traceback
import urllib
import urllib2
import urlparse
import json
import subprocess
import threading
import socket
import ssl

from datetime import datetime, timedelta
from functools import wraps
from xml.dom import minidom

from tornado import httpclient, ioloop, iostream, gen, web
from tornado.httputil import url_concat
from tornado.httputil import HTTPHeaders
from tornado.httpclient import HTTPRequest
from tornado.stack_context import ExceptionStackContext
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.escape import utf8

from . import __version__
from . import __version_info__

from . import utils
from . import config
from . import db
from . import xmpp
from . import http
from . import xmpp_commands
from . import xmpp_handlers
from . import xmpp_stan
