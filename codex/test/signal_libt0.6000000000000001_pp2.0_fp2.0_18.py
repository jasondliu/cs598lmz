import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import os.path
import time
import re
import urllib
import httplib
import urlparse
import threading
import socket
import SimpleHTTPServer
import BaseHTTPServer

from google.appengine.api import urlfetch
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

urlp = re.compile(r'<a href="([^"]+)">', re.I)

class MainPage(webapp.RequestHandler):
    def get(self, path):
        if path == '':
            path = 'index.html'
        if not path.endswith('.html'):
            self.redirect('/')
            return
        f = open(os.path.join(os.path.dirname(__file__), path))
