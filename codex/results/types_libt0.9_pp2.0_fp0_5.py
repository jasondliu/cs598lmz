import types
types.FileType = file
import struct

import socket
from google.appengine.api import apiproxy_stub_map
from google.appengine.api.app_identity import get_application_id
from google.appengine.tools import dev_appserver_index
from google.appengine.tools import dev_appserver_main
from google.appengine.tools.devappserver2 import wsgi_server

try:
  from django.views import debug
except ImportError:
  from django.views import debug as old_debug

  class debug(old_debug):
    def technical_500_response(self, request, *args, **kwargs):
      return super(debug, self).technical_500_response(request, *args, **kwargs)

class ErrorHandler(object):
  def __init__(self, app, host, port, evthdlr):
    self.app = app
    self.host = host
    self.port = port
    self.evthdlr = evthdlr

  def __call__(self, environ, start
