import ctypes
# Test ctypes.CFUNCTYPE as this was the issue for issue20453.
IS_HRESULT = ctypes.c_int
IS_PBOOL = ctypes.POINTER(ctypes.c_int)
class IS_LPVOID(ctypes.c_void_p):
    pass
class IS_PSTR(ctypes.c_char_p):
    pass
CFUNCTYPE_ACCESSOR_HELPER = ctypes.CFUNCTYPE(IS_HRESULT,
                                             IS_PBOOL,
                                             IS_LPVOID,
                                             IS_PSTR,
                                             IS_PSTR)

ctypes_accessor_helper = CFUNCTYPE_ACCESSOR_HELPER

import pickle
import datetime
try:
    cPickle = pickle.cPickle
except AttributeError:
    cPickle = pickle

import platform
import warnings
warnings.filterwarnings("error", "is reentrant", RuntimeWarning,
                        "abcshlib._abcshlib.*")

