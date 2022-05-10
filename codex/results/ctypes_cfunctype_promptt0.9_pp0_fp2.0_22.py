import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)

if sys.platform == 'win32':
    prototype = ctypes.CFUNCTYPE(ctypes.c_long, ctypes.c_long, ctypes.c_long)
    parameters = (1, 2)
else:
    prototype = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)
    parameters = (None,)

def callback(a):
    print(str(a) + ' called')
    return 0

# This creates a bound C function out of 'callback'
CMPFUNC = prototype(callback)

# Comparing pointers to C functions works as expected
print(CMPFUNC == callback)

# Calling it works too

if sys.platform == 'win32':
    CMPFUNC(*parameters)
else:
    CMPFUNC(*parameters)
