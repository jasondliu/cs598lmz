import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)

# https://docs.python.org/3/library/ctypes.html#ctypes.CDLL
# https://docs.python.org/3/library/ctypes.html#ctypes.CDLL.set_concurrency
# https://docs.python.org/3/library/ctypes.html#ctypes.CDLL.set_lazy_dlopen
# https://docs.python.org/3/library/ctypes.html#ctypes.CDLL.set_thread_local
# https://docs.python.org/3/library/ctypes.html#ctypes.CDLL.set_thread_local_direct
# https://docs.python.org/3/library/ctypes.html#ctypes.CDLL.set_thread_local_implicit
# https://docs.python.org/3/library/ctypes.html#ctypes.CDLL.set_thread_local_none
# https://docs.python.org/3/library/ctypes.html#ctypes.CDLL.set_
