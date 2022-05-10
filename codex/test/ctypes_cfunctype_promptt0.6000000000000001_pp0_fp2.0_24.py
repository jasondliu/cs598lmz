import ctypes
# Test ctypes.CFUNCTYPE (issue #13390).
def test_CFUNCTYPE():
    import _ctypes
    API = [('f', ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int))]
    dll = ctypes.CDLL(_ctypes.__file__)
    try:
        dll.f.argtypes = (ctypes.c_int,)
        dll.f.restype = ctypes.c_int
    except AttributeError:
        pass
    else:
        raise Exception


