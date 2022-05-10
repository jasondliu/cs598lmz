import codecs
codecs.register_error('replace', lambda e: u'?')

import platform

try:
    # python3
    from queue import Queue
except ImportError:
    # python2
    from Queue import Queue

import json
import base64
import hashlib
import threading
import os
import urllib
import urllib2
import urlparse
import cgi
import posixpath
import re

from gzip import GzipFile

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

from ws4py.server import WebSocketWSGIApplication
from ws4py.websocket import WebSocket

from ws4py.exc import HandshakeError
import ws4py.server.wsgiutils
import ws4py.server.wsgirefserver

from websocket_server.websocket_handler import WebsocketServerWSGIRequestHandler
from websocket_server.thread_pool import ThreadPool, PoolWorker
import websocket_server.mongrel2_conn as mongrel2_conn
import websocket_server.mongrel2_pub
