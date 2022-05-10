import ctypes
# Test ctypes.CFUNCTYPE, ctypes.cast and 
# POINTER(c_int) in one swoop.

from ctypes import *

def test(v):
    if sys.platform == 'win32':
        # Windows wants the entrypoint name, not the
        # exported symbol.  The entrypoint name is
        # underscore + symbol * 2
        import _testcapi
        dll = CDLL(_testcapi.__file__)
        func_name = '_' + _testcapi.testfunc.__name__ * 2
    else:
        dll = CDLL(ctypes.util.find_library('dl'))
        func_name = 'dlsym'

    func = CFUNCTYPE(POINTER(c_int))(
        c_int.in_dll(dll, func_name))

    v = cast(func(None), POINTER(c_int))
    # the following raises AttributeError on 64-bit platforms
    # because the c_int is too small to hold a pointer value
    try:
        if v[0] != 101:
            raise
