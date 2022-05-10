import ctypes
# Test ctypes.CFUNCTYPE

class X(ctypes.Structure):
    _fields_ = [("p", ctypes.c_void_p),
                ("n", ctypes.c_int)]

def func(a, b, c):
    return a + b + c

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int,
                           ctypes.POINTER(X),
                           ctypes.POINTER(X),
                           ctypes.c_void_p)

cmp_func = CMPFUNC(func)
print cmp_func(None, None, None)

# Test ctypes.PYFUNCTYPE

def py_func(a, b, c):
    return a + b + c

PYFUNC = ctypes.PYFUNCTYPE(ctypes.c_int,
                           ctypes.POINTER(X),
                           ctypes.POINTER(X),
                           ctypes.c_void_p)

py_func = PYFUNC(py_func)
print py_
