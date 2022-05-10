import ctypes
# Test ctypes.CFUNCTYPE()
#
# "PF" is a function pointer type.
#
# XXX: we need to call the ctypes function, because otherwise
# ctypes doesn't detect the function pointer type.
# (This is a known bug in ctypes, reported in SF bug #1888667).

import _ctypes_test

def func(a,b):
    return 1

# XXX: we need to call the ctypes function, because otherwise
# ctypes doesn't detect the function pointer type.
# (This is a known bug in ctypes, reported in SF bug #1888667).

f = _ctypes_test.PF(func)
assert f(1,2) == 1

# Now try a different calling convention
c_stdcall_func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
assert c_stdcall_func(1,2) == 1

# On Windows, calling a function pointer with the wrong calling convention
# causes a crash.  On UNIX, it raises a TypeError.

