import ctypes
# Test ctypes.CFUNCTYPE(...)

def func(*args):
    print args

CALLBACK = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_int)
cb = CALLBACK(func)
cb(1, 2, 3)

# Test ctypes.PYFUNCTYPE(...)

CALLBACK = ctypes.PYFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_int)
cb = CALLBACK(func)
cb(1, 2, 3)

# Test ctypes.CFUNCTYPE(..., use_errno=True)

def func(*args):
    print args

CALLBACK = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_int, use_errno=True)
cb = CALLBACK(func)
cb(1, 2, 3)

# Test ctypes.PYFUNCTYPE(..., use_errno=
