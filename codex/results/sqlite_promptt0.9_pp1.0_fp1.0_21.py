import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() before this import.
import HTMLParser
import httplib
import json
import logging
import math
import os
import random
import re
import shutil
import socket
import stat
import subprocess
import sys
import time
import traceback
import urllib
import urllib2
import urlparse

if sys.platform.startswith('linux'):
    import fcntl

logger = logging.getLogger('common')

class Common:

    def __init__(self, options, args):
        self.options = options
        self.args = args
        self.orig_cwd = os.getcwd()
        self.opener = None
        self.use_free_space = None

        # The following attributes are set later.
        self.build_dir = None
        self.cachedir = None
        self.download_cache = None
        self.dll_path = None
        self.dll_ver_files = None
        self.host_dll_path = {}
        self.host_lib_path = {}
        self.host
