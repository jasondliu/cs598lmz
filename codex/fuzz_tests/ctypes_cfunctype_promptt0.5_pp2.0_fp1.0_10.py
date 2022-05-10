import ctypes
# Test ctypes.CFUNCTYPE

@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def func(i):
    return i

func.__name__ = "func"

# Test ctypes.PYFUNCTYPE

@ctypes.PYFUNCTYPE(ctypes.py_object, ctypes.py_object)
def pyfunc(i):
    return i

pyfunc.__name__ = "pyfunc"

# Test ctypes.WINFUNCTYPE

@ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int)
def winfunc(i):
    return i

winfunc.__name__ = "winfunc"

# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, restype=ctypes.c_int)

@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, restype=ctypes.c_int)
def func2(i):
   
