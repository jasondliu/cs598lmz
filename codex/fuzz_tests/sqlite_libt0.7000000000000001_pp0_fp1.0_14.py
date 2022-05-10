import ctypes
import ctypes.util
import threading
import sqlite3
import logging

logger = logging.getLogger(__name__)

# thread-local storage
class _TLS:
    def __init__(self, storage={}):
        self.storage = storage
    def __getattr__(self, name):
        return self.storage[name]
    def __setattr__(self, name, value):
        if name == "storage":
            self.__dict__[name] = value
        else:
            self.storage[name] = value
tls = threading.local()

# Set the thread-local storage for the current thread.
def set_tls(**kw):
    for k, v in kw.items():
        setattr(tls, k, v)

# Return the thread-local storage for the current thread.
def get_tls():
    return tls.storage

def _get_tracemalloc_symbols():
    c_va_list_p = ctypes.POINTER(ctypes.c_void_p)
    libc = ctypes.CDLL
