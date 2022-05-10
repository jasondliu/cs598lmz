import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 3

import sys
import os
import re
import time
import threading
import traceback
import warnings
import weakref
import gc

# SOURCE LINE 14

import __builtin__

# SOURCE LINE 16

import greenlet

# SOURCE LINE 18

from eventlet import api
from eventlet import hubs
from eventlet import patcher
from eventlet import util
from eventlet import debug
from eventlet import greenthread
from eventlet import semaphore
from eventlet import queue
from eventlet import pools
from eventlet import hubs
from eventlet import greenpool
from eventlet import coros
from eventlet import timeout

# SOURCE LINE 31

__patched__ = ['socket', 'ssl', 'select', 'thread', 'threading', 'Queue', 'subprocess', 'time', 'select', 'os', 'signal']

# SOURCE LINE 34

__imports__ = __patched__ + ['Queue', 'thread', 'threading', 'subprocess', 'time', 'select
