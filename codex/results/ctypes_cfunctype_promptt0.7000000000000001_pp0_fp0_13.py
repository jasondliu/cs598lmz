import ctypes
# Test ctypes.CFUNCTYPE
if sys.platform == "win32":
    from _ctypes import FUNCFLAG_CDECL
else:
    from _ctypes import FUNCFLAG_CDECL, FUNCFLAG_USE_ERRNO

from _ctypes_test import func, funcptr

def callback(arg):
    return arg*2

# C callback function
CBFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

functype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
# XXX Temporarily disabled.  ctypes doesn't support byref(x)
#     in callbacks.
##class X(ctypes.Structure):
##    _fields_ = [("x", ctypes.c_int),
##                ("y", ctypes.c_int)]
##
##    def __ctypes_from_outparam__(self):
##        return ctypes.byref(self)

def check_errno(result, func, arguments):
    import
