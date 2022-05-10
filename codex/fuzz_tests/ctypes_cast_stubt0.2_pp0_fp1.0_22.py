import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 4

import os
import sys
import time
import threading
import traceback
import warnings
import weakref

# SOURCE LINE 13

import __builtin__

# SOURCE LINE 15

from greenlet import greenlet

# SOURCE LINE 17

from eventlet import api
from eventlet import hubs
from eventlet import patcher
from eventlet import util

# SOURCE LINE 22

__patched__ = ['Queue', 'thread', 'threading', '_threading_local', 'dummy_thread', 'dummy_threading']

# SOURCE LINE 27

# This is a threading.local that works with green threads.
# It's implemented as a dictionary that's keyed by greenlet objects.
class local(object):
    __slots__ = ['_local__args', '_local__lock', '_local__storage']
    def __init__(self):
        object.__setattr__(self, '_local__storage', {})
        object.__setattr__(
