import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_uint64)

# import the C library
import os
libpath = os.path.abspath('../lib/libcounter.so')
lib = ctypes.cdll.LoadLibrary(libpath)

# Define Python aliases for the C functions.
# (since I can't use the ctypes.CFUNCTYPE
#  method in the Python interface, I resort
#  to the uglier method of manually
#  redefining the function pointer types)
get_count = lib.get_count
get_count.restype = ctypes.c_uint64

set_count = lib.set_count
set_count.argtypes = [ctypes.c_uint64]

py_incr_count = lib.incr_count
py_incr_count.argtypes = [ctypes.c_uint64]
py_incr_count.restype = ctypes.c_uint64

py_decr_count = lib.decr_count
py_decr_count.argtypes = [ctypes.c_uint64]
