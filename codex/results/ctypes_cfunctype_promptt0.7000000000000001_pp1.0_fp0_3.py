import ctypes
# Test ctypes.CFUNCTYPE()

@ctypes.CFUNCTYPE(None)
def foo():
    pass

foo()

@ctypes.CFUNCTYPE(ctypes.c_int)
def bar():
    return 42

assert bar() == 42
