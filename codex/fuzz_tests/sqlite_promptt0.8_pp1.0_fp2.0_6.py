import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:').execute('select 1')

# libc = ctypes.CDLL(ctypes.util.find_library('c'))
# pthread_create = libc.pthread_create
# pthread_cancel = libc.pthread_cancel

# pthread_create.argtypes = [ctypes.POINTER(ctypes.c_long),
#         ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
# pthread_create.restype = ctypes.c_int

# pthread_cancel.argtypes = [ctypes.c_long]
# pthread_cancel.restype = ctypes.c_int

# def run_in_thread(func, *args):
#     func_ptr = ctypes.CFUNCTYPE(None, ctypes.c_void_p)(func)
#     arg_ptr = ctypes.cast(args, ctypes.c_void_p)
#     pthread_create(None, None, func_ptr,
