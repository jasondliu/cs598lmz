import ctypes
# Test ctypes.CFUNCTYPE configuration
#
# 1. c_int64 (default)
# 2. c_int64.value
# 3. c_int64.value, c_int64(0)
# 4. c_int64.value, c_int64(0), c_bool(False)
# 5. c_int64.value, c_int64(0), c_bool(False), c_bool(False)
# 6. c_int64.value, c_int64(0), c_bool(False), c_bool(False), c_int64(0)

# Used to go to the right place in the test
ERROR_SEQUENCE = __name__ + '.ERROR_SEQUENCE'

CFUNCTYPE_DEFAULTS = ctypes.CFUNCTYPE(c_int64)
CFUNCTYPE_1 = ctypes.CFUNCTYPE(c_int64, c_int64.value)
CFUNCTYPE_2 = ctypes.CFUNCTYPE(c_int64, c_int64.value, c_int64(
