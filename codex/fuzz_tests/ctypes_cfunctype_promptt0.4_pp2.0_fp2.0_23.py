import ctypes
# Test ctypes.CFUNCTYPE()
try:
    ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
except TypeError:
    print('SKIP')
    raise SystemExit

# Test ctypes.CFUNCTYPE() with restype=None
try:
    ctypes.CFUNCTYPE(None, ctypes.c_int)
except TypeError:
    print('SKIP')
    raise SystemExit

# Test ctypes.CFUNCTYPE() with argtypes=None
try:
    ctypes.CFUNCTYPE(ctypes.c_int, None)
except TypeError:
    print('SKIP')
    raise SystemExit

# Test ctypes.CFUNCTYPE() with argtypes=None and restype=None
try:
    ctypes.CFUNCTYPE(None, None)
except TypeError:
    print('SKIP')
    raise SystemExit

# Test ctypes.CFUNCTYPE() with argtypes=None and restype=None
try:
    ctypes.CFUNCTY
