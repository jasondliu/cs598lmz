import socket
import sys
import time

from . import constants
from . import exceptions
from . import utils
from . import version
from . import __version__

try:
    import ssl
except ImportError:
    ssl = None

try:
    import urllib.parse as urlparse
except ImportError:
    import urlparse

try:
    import http.client as httplib
except ImportError:
    import httplib

try:
    import queue
except ImportError:
    import Queue as queue

try:
    import threading
except ImportError:
    import dummy_threading as threading

try:
    import socketserver
except ImportError:
    import SocketServer as socketserver

try:
    import selectors
except ImportError:
    import selectors2 as selectors

try:
    import ssl
except ImportError:
    ssl = None

try:
    import certifi
except ImportError:
    certifi = None

try:
    import urllib3
except ImportError:
    urllib
