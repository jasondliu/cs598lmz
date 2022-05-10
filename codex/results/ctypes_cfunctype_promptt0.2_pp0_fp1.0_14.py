import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument
# the function pointer is passed as None
# this should raise a TypeError
try:
    lib.fp_test(None)
except TypeError:
    pass
else:
    raise RuntimeError("should have raised TypeError")

# call a function with a function pointer argument
# the function pointer is passed as a Python int
# this should raise a TypeError
try:
    lib.fp_test(42)
except TypeError:
    pass
else:
    raise RuntimeError("should have raised TypeError")

# call a function with a function pointer argument
# the function pointer is passed as a ctypes instance
# this should raise a TypeError
try:
    lib.fp_test(lib.my_callback)
except TypeError:
    pass
else:
    raise RuntimeError("should have raised TypeError")

# call a function with a function pointer argument
# the function pointer is passed as a ctypes CFUNCTYPE
