import codecs
codecs.register_error('strict', codecs.ignore_errors)

import os
import sys
import shutil
import subprocess
import re
import os.path
import urllib
import urllib2
import urlparse
import json
import posixpath
import hashlib
import logging
import fnmatch
import datetime
import tempfile
import errno
import stat
import time
import platform
import argparse
import zipfile
import fnmatch

try:
    import requests
except ImportError:
    requests = None

if sys.platform == 'win32':
    import ctypes
    import ctypes.wintypes

logger = logging.getLogger('cordova')

def sha1_file(path):
    with open(path, 'rb') as f:
        return hashlib.sha1(f.read()).hexdigest()

def sha1_git(path):
    p = subprocess.Popen(['git', 'ls-tree', '-r', '--full-tree', '--name-only', 'HEAD', path], stdout=subprocess
