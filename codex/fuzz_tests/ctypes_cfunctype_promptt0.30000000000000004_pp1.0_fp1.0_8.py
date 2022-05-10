import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# Call a function with a simple argument

lib.set_errno.argtypes = (ctypes.c_int,)
lib.set_errno.restype = None

lib.set_errno(42)
print(ctypes.get_errno())

# Call a function with a pointer argument

lib.set_errno_v2.argtypes = (ctypes.POINTER(ctypes.c_int),)
lib.set_errno_v2.restype = None

p = ctypes.c_int(42)
lib.set_errno_v2(p)
print(ctypes.get_errno())

# Call a function with a pointer argument

lib.set_errno_v3.argtypes = (ctypes.POINTER(ctypes.c_int),)
lib.set_errno_v3.restype = None

p = ctypes.c_int(42)
lib.set
