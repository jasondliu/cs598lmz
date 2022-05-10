import ctypes
# Test ctypes.CFUNCTYPE.
#
# In this test, we are just checking that the CFUNCTYPE object itself
# can be passed around and used as a function pointer.  We don't care
# about the results of calling the function itself.
#
# The system C library version of printf() may be called when the
# function cannot be executed, so we need to pipe stderr away.

import sys, os

libc = ctypes.CDLL(None)

@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)
def funcptr(msg):
    print(msg)
    return len(msg)

libc.printf(b"calling funcptr(b'abc')\n")
libc.printf(b"%d\n", funcptr(b"abc"))

if os.name == "nt":
    import _ctypes
    libc.printf.errcheck = _ctypes.missing

try:
    libc.printf(b"%d\n", funcptr)
except AttributeError:
    print("C
