import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

r = fun()
assert r == "hello"

# issue #1810: crash in ctypes.CFUNCTYPE()

lib = ctypes.CDLL(ctypes.util.find_library("c"))

cb_type = ctypes.CFUNCTYPE(ctypes.c_int)
cb_func = cb_type(lambda x: 0)

lib.qsort.argtypes = [ctypes.c_void_p, ctypes.c_size_t, ctypes.c_size_t, cb_type]
lib.qsort.restype = None

lib.qsort(0, 0, 0, cb_func)

# issue #1846: calling into ctypes from PyPy cpyext

import _rawffi
class UnsignedLongLong(ctypes.c_ulonglong):
    @classmethod
    def from_param(cls, value):
        if isinstance(value, ctypes.c_void_p):
            return ctypes.cast(value, cls)

