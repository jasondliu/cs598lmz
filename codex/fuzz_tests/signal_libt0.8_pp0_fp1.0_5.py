import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import sys
import hashlib
import getpass
import json
import mimetypes
import urllib
import socket
import tempfile
import threading
import multiprocessing
import subprocess
import xml.etree.ElementTree as ET

from collections import namedtuple
from time import time
from urllib import unquote
from urllib2 import Request, urlopen, URLError
from httplib import HTTPConnection, HTTPException
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui_cloud import Ui_Cloud


class Command(object):
    """Encapsulates a system command-line."""
    def __init__(self, command):
        self.command = command

    def run(self, shell=True):
        """Execute the command."""
        process = subprocess.Popen(self.command, shell=shell,
