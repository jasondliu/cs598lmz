import ctypes
import ctypes.util
import threading
import sqlite3
import re
import os
import signal
import ConfigParser
import shutil
import signal
import time
import logging
import struct
import sys
import traceback
from optparse import OptionParser

from urlparse import urlparse
from httplib import HTTPConnection, HTTPException

from SocketServer import ThreadingMixIn
from SimpleHTTPServer import SimpleHTTPRequestHandler, test as _test
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import BaseServer

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    def __init__(self, host, port, data_dir, http_handler):
        HTTPServer.__init__(self, (host, port), http_handler)
        self.data_dir = data_dir
        self.server_name = "ThreadingHTTPServer"
        self.daemon_threads = True
        self.allow_reuse_address = True

class HTTPHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        path = path.split('?',1)[0]
        path
