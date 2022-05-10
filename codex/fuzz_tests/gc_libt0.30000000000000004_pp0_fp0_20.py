import gc, weakref
import sys
import time
import traceback
import types
import unittest

from test import support

# The module is called 'threading' in Python 2.
threading = support.import_module('threading')

# This is a hack to keep our thread counts accurate.
_counter_lock = threading.Lock()
_active_limbo_lock = _counter_lock
_limbo = {}
_active = {}
_dangling = weakref.WeakKeyDictionary()

def _cleanup():
    _active_limbo_lock.acquire()
    try:
        for thr in list(_limbo.keys()):
            _join_exited_thread(thr)
    finally:
        _active_limbo_lock.release()

atexit.register(_cleanup)

def _remove_dead_thread(thr):
    _active_limbo_lock.acquire()
    try:
        _active.pop(thr, None)
        _limbo.pop(thr, None)
    finally:
        _active_lim
