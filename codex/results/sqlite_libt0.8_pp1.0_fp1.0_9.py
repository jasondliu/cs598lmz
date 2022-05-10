import ctypes
import ctypes.util
import threading
import sqlite3
import string
import numbers
import platform
import os
import os.path
import re
import sys
import json
import argparse
import subprocess
import pkg_resources
import codecs
import mimetypes
import tempfile

from . import __version__
from .config import Config
from .command import Command
from .compatibility import *
from .utils import *
from .logger import *

__all__ = ['DumbHTTPProxy']

class HTTPProxyHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP proxy handler."""
    
    @property
    def server_version(self):
        return 'DumbHTTPProxy/' + __version__
    
    def do_CONNECT(self):
        """Handle "CONNECT" request."""
        if not self.try_local_proxy():
            self.try_remote_proxy()
    
    def try_local_proxy(self):
        """Try proxy the request to local proxy server."""
        if not self.server.local_proxy:
            return False
        if self.path.startswith
