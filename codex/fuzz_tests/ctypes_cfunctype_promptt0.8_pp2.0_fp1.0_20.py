import ctypes
# Test ctypes.CFUNCTYPE().

import _ctypes_test

try:
    c = ctypes.cdll.msvcrt
except:
    raise ImportError("msvcrt not found")

Callable = ctypes.CFUNCTYPE(ctypes.c_int)

class X:
    def __init__(self):
        self.called = 0

    def __call__(self, arg):
        self.called += 1
        return arg

x = X()

@Callable
def func(arg):
    x.called += 1
    return arg

for arg in (-5, -1, 0, 3, 5):
    assert func(arg) == arg
    assert x.called == 1
    assert func(arg) == arg
    assert x.called == 2
    assert _ctypes_test.callit(Callable, arg) == arg
    assert x.called == 3

# bpo-36879: A new class only used to wrap functions should not be subtyped.
# In this case, the PyCFuncPtrBase class is used to wrap the
