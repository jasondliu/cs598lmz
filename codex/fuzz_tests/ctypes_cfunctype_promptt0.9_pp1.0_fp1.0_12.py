import ctypes
# Test ctypes.CFUNCTYPE

if os.name == 'nt':
    import _ctypes_test
else:
    from _ctypes_test import RPythonAnnotator

def test_structure_getattr():
    class X(ctypes.Structure):
        _fields_ = [("a", ctypes.c_int)]
        def __repr__(self):
            return "<%s>" % (self.a)
    x = X()
    x.a = 42
    assert repr(x) == "<42>"
    assert repr(X(a=42)) == "<42>"

def test_structure_with_dict():
    class X(ctypes.Structure):
        _fields_ = [("a", ctypes.c_int)]
    class Y(X, ctypes.Structure):
        _pack_ = 1
        _fields_ = [("b", ctypes.c_int)]
    x = X()
    y = Y()
    assert y.a
    assert y.a == 0
    y.a = 5
    #
    raises(AttributeError
