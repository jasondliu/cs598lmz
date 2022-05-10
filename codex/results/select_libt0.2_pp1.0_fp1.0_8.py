import select
import socket
import sys
import threading
import time
import traceback
import urllib
import urlparse

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn
from SimpleHTTPServer import SimpleHTTPRequestHandler

from . import __version__
from . import config
from . import log
from . import util
from . import web_ui

logger = log.get_logger(__name__)

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    pass

class WebServer(object):
    def __init__(self, config_dir, data_dir, port, address,
                 web_ui_dir, web_ui_port, web_ui_address,
                 web_ui_password, web_ui_password_salt,
                 web_ui_password_hash_method,
                 web_ui_no_password,
                 web_ui_rest_api_enabled,
                 web_ui_rest_api_cors_origins,
                 web_ui_rest_api_cors
