import ctypes
# Test ctypes.CFUNCTYPE
# XXX I don't know how to do this check for real.  At least run it...
try:
    CFUNCTYPE = ctypes.CFUNCTYPE
except AttributeError:
    pass
else:
    import sys
    import _testcapi
    if sys.platform == 'win32':
        # XXX Should cdll.msvcrt.getch also be supported?
        lib = ctypes.cdll.LoadLibrary('msvcrt')
        if not hasattr(lib, 'getch'):
            lib = ctypes.cdll.LoadLibrary('kernel32')
    else:
        lib = ctypes.cdll.LoadLibrary(None)

    CMPFUNC = CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
    def py_cmp_func(a, b):
        x,y = ctypes.cast(a, ctypes.POINTER(ctypes.c_int)), \
              ctypes.cast(b, ctypes.POINTER(ctypes
