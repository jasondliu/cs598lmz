import ctypes
# Test ctypes.CFUNCTYPE() objects.  These are a bit different
# because the argtypes are not stored as a tuple, but in a separate
# list.  This means that we need to use another strategy to check that
# they work as expected.
#
def callback(number):
    print 'callback(%d)' % number
    return -number
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
callbackfunc = CALLBACKFUNC(callback)
import _ctypes_test
_ctypes_test.set_callback(callbackfunc)
_ctypes_test.call_callback(42)
try:
    _ctypes_test.call_callback((1,))
except TypeError:
    pass
else:
    raise RuntimeError("expected TypeError")
