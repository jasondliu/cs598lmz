import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello World"

@FUNTYPE
def fun2():
    return None

from ctypes import _CFuncPtr
assert isinstance(fun, _CFuncPtr)

try:
    fun()
except TypeError:
    import sys
    print(sys.exc_info())

assert fun2() is None

@FUNTYPE
def fun3(a):
    return a

assert fun3(42) == 42

@FUNTYPE
def fun4(a, b):
    return a, b

assert fun4(1, 2) == (1, 2)

# test calling convention

try:
    FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, calling_convention='foo')
except ValueError:
    pass
else:
    raise RuntimeError("should have raised ValueError")

try:
    FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, use_errno=True)
except ValueError:
    pass
else:
    raise RuntimeError("should have raised ValueError")
