import socket
import sys
import threading
import time
import traceback

from . import constants
from . import exceptions
from . import utils
from . import version
from . import websocket
from . import websocket_client
from . import websocket_server
from . import websocket_thread

try:
    import ssl
except ImportError:
    ssl = None

try:
    import queue
except ImportError:
    import Queue as queue

try:
    import http.client as httplib
except ImportError:
    import httplib

try:
    import urllib.parse as urlparse
except ImportError:
    import urlparse

try:
    import socketserver
except ImportError:
    import SocketServer as socketserver

try:
    import http.server as SimpleHTTPServer
except ImportError:
    import SimpleHTTPServer

try:
    import http.server as BaseHTTPServer
except ImportError:
    import BaseHTTPServer

try:
    import http.cookies as Cookie
except ImportError:
    import Cookie

