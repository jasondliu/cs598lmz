import ctypes
# Test ctypes.CFUNCTYPE(...)

def test_CFUNCTYPE_return():
    CFUNCTYPELIB = ctypes.WinDLL(None, use_errno=True)
    "Test CFUNCTYPE(None, ...)"

    # return types

    f = CFUNCTYPELIB.msvcrt.printf
    assert f.argtypes is None
    assert f.restype == ctypes.c_int

    f = CFUNCTYPELIB.msvcrt.sprintf
    assert f.argtypes is None
    assert f.restype == ctypes.c_char_p

    # cdll.LoadLibrary(None) is a temporary hack for Python 2.4

def test_CFUNCTYPE_errcheck():
    from ctypes import c_int, c_char_p
    lib = ctypes.c_int(0)
    f = CFUNCTYPE(c_int, c_char_p)
    # The _testfunc_ is just a dummy here.
