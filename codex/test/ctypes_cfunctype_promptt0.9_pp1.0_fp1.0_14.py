import ctypes
# Test ctypes.CFUNCTYPE
import _ctypes_test

import sys
if sys.platform.startswith("win"):
    stdcall = ctypes.WINFUNCTYPE
else:
    stdcall = ctypes.CFUNCTYPE

@stdcall(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def func(a, b):
    print("func(%d, %d) called" % (a, b))
    return 2 * a - b

class Z:
    def __init__(self):
        self.value = 42

def test():
    for atype in _ctypes_test.types:
        if atype is ctypes.c_void_p:
            continue
        func.argtypes = py_object, atype
        func.restype = atype

        obj = Z()
        res = func(obj, 0)
        assert res == 0

        func(obj, 1)
        res = func(obj, 2)
        assert res == 2

        res = func(obj, -1)
       
