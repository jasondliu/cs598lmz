import ctypes
# Test ctypes.CFUNCTYPE(None)

def test_CFUNCTYPE_None(lib):
    f = ctypes.CFUNCTYPE(None)(lambda: None)
    f()
    assert f() is None

def test_CFUNCTYPE_None_arg(lib):
    f = ctypes.CFUNCTYPE(None, ctypes.c_int)(lambda x: None)
    f(0)
    assert f(1) is None

def test_CFUNCTYPE_None_restype(lib):
    f = ctypes.CFUNCTYPE(None, restype=None)(lambda: None)
    f()
    assert f() is None

def test_CFUNCTYPE_None_arg_restype(lib):
    f = ctypes.CFUNCTYPE(None, ctypes.c_int, restype=None)(lambda x: None)
    f(0)
    assert f(1) is None

def test_CFUNCTYPE_None_arg_restype_errcheck(lib):
    f = c
