import ctypes
ctypes.cast(p, ctypes.py_object).value

from ctypes import pythonapi, py_object

p = {'hello': 'world'}

py_object = ctypes.py_object
pythonapi.PyObject_AsReadBuffer.restype = ctypes.c_int
pythonapi.PyObject_AsReadBuffer.argtypes = [py_object, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_size_t)]

c_void_p = ctypes.c_void_p()
c_size_t = ctypes.c_size_t()

pythonapi.PyObject_AsReadBuffer(py_object(p), ctypes.byref(c_void_p), ctypes.byref(c_size_t))

c_void_p.value, c_size_t.value



# enumerate

from ctypes import *
from ctypes.util import find_library

libc = CDLL(find_library('c'))

LONG = c_long
P
