import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

class X(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("y", ctypes.c_int)]

def callback(x, y):
    print(x, y)

# calling convention
if sys.platform == "win32":
    CALLBACK = ctypes.WINFUNCTYPE
else:
    CALLBACK = ctypes.CFUNCTYPE

cb = CALLBACK(None, ctypes.POINTER(X), ctypes.POINTER(Y))

cb(X(1), Y(2))
cb(X(3), Y(4))
print(cb)

# calling convention
if sys.platform == "win32":
    CALLBACK = ctypes.WINFUNCTYPE
else:
    CALLBACK = ctypes.CFUNCTYPE

cb = CALLBACK(None, ctypes.POINTER(X), ctypes.POINTER(Y))

cb(X(1), Y(2
