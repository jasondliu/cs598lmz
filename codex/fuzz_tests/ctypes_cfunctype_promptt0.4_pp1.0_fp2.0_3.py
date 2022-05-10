import ctypes
# Test ctypes.CFUNCTYPE

if __name__ == "__main__":
    import sys
    import os

    if sys.platform == "win32":
        import _winapi
        # don't open a message box on failure
        _winapi.SetErrorMode(_winapi.SEM_FAILCRITICALERRORS)

    #
    # Test basic CFUNCTYPE
    #
    from ctypes import *
    prototype = CFUNCTYPE(c_int, c_int, c_int)
    paramflags = (1, "x"), (1, "y")

    #
    # Test CFUNCTYPE with restype=None
    #
    prototype = CFUNCTYPE(None, c_int, c_int)
    paramflags = (1, "x"), (1, "y")

    #
    # Test CFUNCTYPE with argtypes=None
    #
    prototype = CFUNCTYPE(c_int)
    paramflags = ()

    #
    # Test CFUNCTYPE with argtypes=None and restype=None
   
