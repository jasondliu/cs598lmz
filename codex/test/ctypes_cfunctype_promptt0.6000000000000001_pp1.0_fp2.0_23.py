import ctypes
# Test ctypes.CFUNCTYPE()

# A Python integer is a C long, so this should be the same as
# CFUNCTYPE(c_long).
PyCFunc = ctypes.CFUNCTYPE(ctypes.py_object)

# This function is defined in C as
#
# long f(long x) {
#     return x * x;
# }
#
# The long return value is converted to a Python integer.
