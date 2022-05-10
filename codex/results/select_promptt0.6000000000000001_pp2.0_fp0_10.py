import select
# Test select.select()
import socket
import sys
import threading
import time
import urllib
import urlparse

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn
from cStringIO import StringIO

import wsgiref.handlers

import google3
import google3.enterprise.legacy.production.babysitter.client as client
from google3.enterprise.legacy.util import C
from google3.enterprise.legacy.util import E
from google3.enterprise.legacy.util import M
from google3.enterprise.tools import M
from google3.pyglib import logging
from google3.enterprise.legacy.util import host_utils
from google3.enterprise.legacy.util import misc
from google3.enterprise.legacy.util import thread_utils
from google3.enterprise.legacy.production.babysitter import config_manager
from google3.enterprise.legacy.production.babysitter import constants
from google3.enterprise.legacy.production.bab
