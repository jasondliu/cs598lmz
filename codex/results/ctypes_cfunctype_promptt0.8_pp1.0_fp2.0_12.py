import ctypes
# Test ctypes.CFUNCTYPE 1st argument's type.
# This should fail to compile.

#pragma(python)
def f():
    CFUNCTYPE(c_int, c_char_p)

f()
