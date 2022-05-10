import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_c_field():
    assert isinstance(S.x, ctypes.CField)

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('x', ctypes.c_int)]

def test_field_names():
    assert S._fields_ == [('x', ctypes.c_int)]

class X(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

def test_class_attributes():
    assert X.__module__ == 'test_ctypes'
    assert X.x.__module__ == 'test_ctypes'
    if sys.version_info > (3,):
        import ctypes.test
        assert X.__qualname__ == 'X'
        assert X.x.__qualname__ == 'S.x'
        assert ctypes.test.__name__ == 'ctypes.test'

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_
