import ctypes
# Test ctypes.CFUNCTYPE
def callback(x, y):
    return x+y

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Python 2.4 requires the additional 'restype' and 'argtypes' attributes to
# be set on the callback function.
callback.restype = ctypes.c_int
callback.argtypes = (ctypes.c_int, ctypes.c_int)

# Test
if callback(5, 5) != 10:
    raise RuntimeError("ctypes.CFUNCTYPE test failed")

# Test ctypes.PYFUNCTYPE
def pycallback(x, y):
    return x+y

PYCALLBACK = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Test
if pycallback(5, 5) != 10:
    raise RuntimeError("ctypes.PYFUNCTYPE test failed")

# Test ctypes.PY_
