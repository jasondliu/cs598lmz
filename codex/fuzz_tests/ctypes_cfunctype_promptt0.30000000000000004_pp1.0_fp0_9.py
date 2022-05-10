import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# XXX This is a hack.  We should really check the type of the
# XXX function pointer.
if ctypes.sizeof(ctypes.c_void_p) == ctypes.sizeof(ctypes.c_long):
    proto = ctypes.CFUNCTYPE(ctypes.c_long)
else:
    proto = ctypes.CFUNCTYPE(ctypes.c_int)

# Test that the function pointer can be called
func = proto(("_testfunc_callback", lib))
res = func()
if res != 42:
    raise Exception("function call failed")

# Test that the function pointer can be passed to another function
res = lib.call_function(func)
if res != 42:
    raise Exception("function call failed")

# Test that the function pointer can be passed to another function
# which is called by a callback
res = lib.call_function_in_callback(func)
if res != 42:
   
