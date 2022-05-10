import ctypes
# Test ctypes.CFUNCTYPE
#
#     void (*func)(void)
#
import _ctypes_test

try:
    import _ctypes_test
except ImportError:
    raise Exception("import _ctypes_test failed")

FUNC = _ctypes_test.FUNC

from ctypes import c_int

def callback(result):
    print(result.value)

def callit(func):
    func()

CALLBACKFUNC = ctypes.CFUNCTYPE(None, c_int)

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def py_cmp(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0


FuncType = ctypes.CFUNCTYPE(None)
f1 = FuncType(callback)
FuncType(callback)

f2 = FuncType(lambda: None)

f3 = Fun
