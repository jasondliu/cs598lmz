import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 3

#fun()

import ctypes
import ctypes.util
cdll = ctypes.CDLL(ctypes.util.find_library('c'))
cdll.puts.argtypes = ctypes.c_char_p,
cdll.puts.restype = ctypes.c_int
#cdll.puts('hello, world')

def register_c_function(name,restype,argtypes):
    cdll.__getattr__(name).restype = restype
    cdll.__getattr__(name).argtypes = argtypes

register_c_function('puts', ctypes.c_int, [ctypes.c_char_p])
#cdll.puts('hello, world')

import ctypes
from ctypes import *
from ctypes.util import find_library

#libc = cdll.LoadLibrary(find_library('c'))
