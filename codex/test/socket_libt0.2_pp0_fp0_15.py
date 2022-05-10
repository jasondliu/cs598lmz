import socket
import sys
import time

from . import exceptions
from . import utils

try:
    import ssl
except ImportError:
    ssl = None

try:
    import httplib
except ImportError:
    import http.client as httplib

try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse

try:
    import Queue as queue
except ImportError:
    import queue

try:
    import thread
except ImportError:
    import _thread as thread

try:
    import SocketServer
except ImportError:
    import socketserver as SocketServer

try:
    import BaseHTTPServer
except ImportError:
    import http.server as BaseHTTPServer

try:
    import SimpleHTTPServer
except ImportError:
    import http.server as SimpleHTTPServer

try:
    import cStringIO as StringIO
except ImportError:
    import io as StringIO

try:
    import cPickle as pickle
except ImportError:
    import pickle

