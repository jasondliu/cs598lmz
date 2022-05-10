import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys
import os
import re
import inspect
from cStringIO import StringIO
import urllib2
import threading

try:
    import faulthandler
except ImportError:
    faulthandler = None

libemacspeak = ctypes.CDLL(ctypes.util.find_library('emacspeak'))

