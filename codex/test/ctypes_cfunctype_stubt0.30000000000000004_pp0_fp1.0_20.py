import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def test_bug_1005():
    # Issue #1005
    assert fun() is None

def test_bug_1059():
    # Issue #1059
    assert ctypes.cast(None, ctypes.c_void_p) is None
    assert ctypes.cast(ctypes.c_void_p(), ctypes.c_void_p) is None

def test_bug_1063():
    # Issue #1063
    class X(ctypes.Structure):
        _fields_ = [("a", ctypes.c_int)]
    x = X()
    x.a = 42
    assert ctypes.cast(x, ctypes.c_void_p).value == ctypes.addressof(x)

