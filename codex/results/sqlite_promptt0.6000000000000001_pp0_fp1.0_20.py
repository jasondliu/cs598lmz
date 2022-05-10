import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

import time
import os
import re
import sys
import signal
import stat
import errno
import itertools
import shutil
import tempfile
import unicodedata
import subprocess
import shlex
import locale

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

try:
    from urllib.parse import quote as urlquote
except ImportError:
    from urllib import quote as urlquote

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

try:
    from urllib.request import HTTPError
except ImportError:
    from urllib2 import HTTPError

try:
    from urllib.request import install_opener
except ImportError:
    from urllib2 import install_opener

try:
    from urllib.request import build_opener
except ImportError:
    from urllib2 import build_opener

try:
    from urll
