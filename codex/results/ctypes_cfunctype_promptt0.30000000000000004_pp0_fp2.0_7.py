import ctypes
# Test ctypes.CFUNCTYPE
import _ctypes_test

lib = CDLL(_ctypes_test.__file__)

# Test prototypes

# int func(int)
prototype = CFUNCTYPE(c_int, c_int)

# int func(int, int)
prototype = CFUNCTYPE(c_int, c_int, c_int)

# int func(int, int, int)
prototype = CFUNCTYPE(c_int, c_int, c_int, c_int)

# int func(int, int, int, int)
prototype = CFUNCTYPE(c_int, c_int, c_int, c_int, c_int)

# int func(int, int, int, int, int)
prototype = CFUNCTYPE(c_int, c_int, c_int, c_int, c_int, c_int)

# int func(int, int, int, int, int, int)
prototype = CFUNCTYPE(c_int, c_int, c_int, c_int
