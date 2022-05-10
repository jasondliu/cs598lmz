import ctypes
# Test ctypes.CFUNCTYPE
def callback(x):
    return x

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(callback)

class X(ctypes.Structure):
    _fields_ = [("c_callback", CALLBACK)]

x = X()
x.c_callback(42)

# Test ctypes.PYFUNCTYPE
def callback(x):
    return x

CALLBACK = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int)(callback)

class X(ctypes.Structure):
    _fields_ = [("c_callback", CALLBACK)]

x = X()
x.c_callback(42)

# Test ctypes.WINFUNCTYPE
def callback(x):
    return x

CALLBACK = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int)(callback)

class X(ctypes.Structure):
    _fields_ = [("c_callback", CALL
