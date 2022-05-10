import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

# Import the library
_lib = ctypes.CDLL(ctypes.util.find_library('pthread'))

# Configure the prototype and parameters of the function 'pthread_create'
# (also known as thread_create)
_lib.pthread_create.argtypes = [ctypes.c_void_p, ctypes.c_void_p,
                                ctypes.c_void_p, ctypes.c_void_p]
_lib.pthread_create.restype = ctypes.c_int

# Configure the prototype and parameters of the function 'pthread_join'
# (also known as thread_join)
_lib.pthread_join.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
_lib.pthread_join.restype = ctypes.c_int

# Configure the prototype and parameters of the function 'pthread_exit'
# (also known as thread_exit)
_lib.pthread_exit.argtypes = [ctypes.c_
