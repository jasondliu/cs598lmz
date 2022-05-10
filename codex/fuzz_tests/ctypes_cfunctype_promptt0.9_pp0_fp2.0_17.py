import ctypes
# Test ctypes.CFUNCTYPE
_cfunctype = ctypes.CFUNCTYPE

def test(debug=False):

    if debug:
        import sys
        sys.stdout.write("\nFUNCTYPE\n")
        _cfunctype.restype = None
        _cfunctype.argtypes = []
        _cfunctype(lambda: None, True)
       _cfunctype.argtypes = [ctypes.c_int]
        _cfunctype(lambda x: None, True)

    # One argument
    PyCFuncPtr = _cfunctype(ctypes.c_int)
    i = PyCFuncPtr(lambda x: 0)
    assert type(i) is int

    # No arguments
    PyCFuncPtr = _cfunctype()
    i = PyCFuncPtr(lambda: 0)
    assert type(i) is int

if (__name__ == "__main__"):
    test()
