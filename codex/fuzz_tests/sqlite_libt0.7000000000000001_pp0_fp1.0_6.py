import ctypes
import ctypes.util
import threading
import sqlite3
import sys

from ctypes import c_void_p, c_char_p, c_int, c_double

_pthread = ctypes.CDLL(ctypes.util.find_library('pthread'), use_errno=True)
_pthread.pthread_self.argtypes = []
_pthread.pthread_self.restype = c_uint

try:
    from ctypes import pythonapi, py_object
except ImportError:
    raise ImportError('No module named ctypes!')

pythonapi.PyThreadState_Get.restype = c_void_p
pythonapi.PyThreadState_Get.argtypes = []

try:
    _c_thread_key = c_uint.in_dll(_pthread, '_pthread_key_t_cached_pid')
except ValueError:
    _c_thread_key = c_uint.in_dll(_pthread, '_pthread_key_t_cached_pid_np')

_c_thread_key_offset = 4

_threading_local =
