import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 3

import sys
import os
import time
import threading
import traceback
import warnings
import weakref
import gc
import __builtin__

# SOURCE LINE 15

import greenlet

# SOURCE LINE 17

from eventlet import api
from eventlet import hubs
from eventlet import patcher
from eventlet import util
from eventlet.support import greenlets as greenlet
from eventlet.support import get_errno

# SOURCE LINE 24

__patched__ = ['socket', 'thread', 'time', 'select', 'ssl', 'httplib', 'BaseHTTPServer', 'SimpleHTTPServer', 'SocketServer', 'signal', 'subprocess', 'threading', 'Queue', 'curses', 'select', 'thread', 'Queue', 'threading', 'Queue', 'threading', 'Queue', 'threading', 'Queue', 'threading', 'Queue', 'threading', 'Queue', 'threading', 'Queue', 'threading', 'Queue', 'threading', 'Queue', 'thread
