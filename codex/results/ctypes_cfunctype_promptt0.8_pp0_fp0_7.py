import ctypes
# Test ctypes.CFUNCTYPE
#
# ctypes.CFUNCTYPE(restype, *argtypes, **kw)

# This code is mostly wrong
#
# The first argument to CFUNCTYPE should be the return type, not the
# argument type.  Wrap this so we can test the fix
def CFUNCTYPE(*args, **kw):
    return ctypes.CFUNCTYPE(args[0], *args[1:], **kw)

ctypes.c_int.value = 5
ctypes.c_int.__call__ = 42

c_int = ctypes.c_int

f = CFUNCTYPE(c_int, c_int)
print f.argtypes
assert f.argtypes == (c_int,)
callit = f(lambda x: x * 2)
assert callit(6) == 12

callit = CFUNCTYPE(c_int, c_int)(lambda x: x * 2)
assert callit(7) == 14

# Check default argtypes
f = CFUNCTYPE(c_int)

