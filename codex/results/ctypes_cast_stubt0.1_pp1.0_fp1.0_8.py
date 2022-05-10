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

# SOURCE LINE 14

import greenlet

# SOURCE LINE 16

from eventlet import api
from eventlet import hubs
from eventlet import patcher
from eventlet import util
from eventlet import debug
from eventlet import greenthread
from eventlet import queue
from eventlet import semaphore
from eventlet import timeout
from eventlet import version

# SOURCE LINE 26

__patched__ = ['Queue', 'sleep', 'spawn', 'spawn_n', 'spawn_after', 'spawn_after_local', 'spawn_link', 'spawn_link_value', 'spawn_link_exception', 'spawn_n', 'spawn_after', 'spawn_after_local', 'spawn_link', 'spawn_link_value', 'spawn_link_exception', 'connect', 'connect_ex', 'coros', 'with_timeout', 'Timeout', 'with
