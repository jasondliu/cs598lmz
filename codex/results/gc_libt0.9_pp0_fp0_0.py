import gc, weakref
from types import FunctionType
from threading import Lock, current_thread
from collections import defaultdict
import Queue

from pyaella import singletons as sing
from pyaella.dinj import ConfigurableFactory


__all__ = [
    'objmap',
    'objdict'
]

__all__ = [
    'ObjMap',
    'ObjDict'
]

class ThreadedObjDict(object):
    """ """
    _lock = Lock()
    _map = {}

    @classmethod
    def get_item(cls, key, default=None):
        with cls._lock:
            return cls._map.get(key, default)

    @classmethod
    def len(cls):
        with cls._lock:
            return len(cls._map)

    @classmethod
    def clear(cls):
        with cls._lock:
            return cls._map.clear()

    @classmethod
    def contains_key(cls, key):
        with cls._lock:
            return key
