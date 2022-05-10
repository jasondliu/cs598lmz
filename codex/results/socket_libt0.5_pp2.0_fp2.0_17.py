import socket
import struct
import subprocess
import sys
import threading
import time
import traceback

from . import __version__

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

import requests

try:
    import dns.resolver
except ImportError:
    dns = None

try:
    from http.client import HTTPConnection
except ImportError:
    from httplib import HTTPConnection

try:
    from http.client import HTTPSConnection
except ImportError:
    from httplib import HTTPSConnection

try:
    from http.server import BaseHTTPRequestHandler, HTTPServer
except ImportError:
    from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

try:
    from socketserver import ThreadingMixIn
except ImportError:
    from SocketServer import ThreadingMixIn

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

try:
    from urllib.request import build_opener
except Import
