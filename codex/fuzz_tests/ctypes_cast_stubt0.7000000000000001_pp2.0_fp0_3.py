import ctypes
ctypes.cast(c_double(1),ctypes.c_void_p).value

##
## 
##

import ctypes
import ctypes.util

def _get_c_fun(name, argtypes, restype):
    f = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c')).__getattr__(name)
    f.argtypes = argtypes
    f.restype = restype
    return f

_malloc = _get_c_fun('malloc', [ctypes.c_size_t], ctypes.c_void_p)
_free = _get_c_fun('free', [ctypes.c_void_p], None)

def malloc(size):
    return ctypes.cast(_malloc(size), ctypes.c_void_p).value

def free(addr):
    _free(ctypes.c_void_p(addr))

##
## 
##

import ctypes

# load the shared library into ctypes
lib = ctypes.cdll.LoadLibrary
