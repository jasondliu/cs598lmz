import mmap
import os
import re
import socket
import subprocess
import sys
import time
import traceback
import urllib
import urlparse

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

import config
import utils

from utils import *
from utils import log, log2, log3

#------------------------------------------------------------------------------

def get_file_size(filename):
    return os.path.getsize(filename)

def get_file_mtime(filename):
    return os.path.getmtime(filename)

def get_file_hash(filename):
    return utils.get_hash(filename)

def get_file_info(filename):
    return (get_file_size(filename), get_file_mtime(filename), get_file_hash(filename))

#------------------------------------------------------------------------------

class Torrent:

    def __init__(self, filename=''):
        self.filename = filename
        self.size = 0
        self.mtime = 0
        self.hash = ''
        self.magnet = None
        self.info
