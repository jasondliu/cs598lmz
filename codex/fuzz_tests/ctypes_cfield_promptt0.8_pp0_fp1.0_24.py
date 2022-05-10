import ctypes
# Test ctypes.CField
def test_CField():
    assert ctypes.CField.__name__ == "_CDataDescriptor"
    #
    class X(ctypes.Structure):
        _fields_ = [("a", ctypes.c_char_p)]
    c = X()
    assert isinstance(X.a, ctypes.CField)
    assert X.a.__name__ == "a"
    assert X.a.__class__ == ctypes.CField
    assert X.a.__objclass__ == X
    assert X.a.__fieldtype__ == ctypes.c_char_p
    assert isinstance(c.a, ctypes.c_char_p)
    #
    class X(ctypes.Structure):
        _fields_ = [("a", ctypes.c_char_p),
                    ("b", ctypes.c_char_p)]
    c = X()
    assert isinstance(X.a, ctypes.CField)
    assert X.a.__name__ == "a"
    assert X.a.__class
