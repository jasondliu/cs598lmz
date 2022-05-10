import ctypes
# Test ctypes.CFUNCTYPE()

# This test is only valid on platforms where sizeof(long) == sizeof(void*)
# (i.e. 32-bit platforms).

def callback(arg):
    print "callback called with argument", arg
    return arg

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_long, ctypes.c_long)

# The following line fails with a TypeError if sizeof(long) != sizeof(void*)
# (i.e. 64-bit platforms).
cb = CALLBACKFUNC(callback)

print cb(42)
