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
f = PyCFunc(("f", dll), ((1,),))
assert f(5) == 25

# This function is defined in C as
#
# long sum(long x, long y) {
#     return x + y;
# }
#
# The long return value is converted to a Python integer.
sum = PyCFunc(("sum", dll), ((1,), (1,)))
assert sum(5, 6) == 11

# This function is defined in C as
#
# long get_pointer(long x) {
#     return (long)&x;
# }
#
# The long return value is converted to a Python
