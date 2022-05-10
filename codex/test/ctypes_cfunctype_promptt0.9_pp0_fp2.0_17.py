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
