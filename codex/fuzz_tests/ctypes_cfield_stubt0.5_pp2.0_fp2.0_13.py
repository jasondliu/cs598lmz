import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self, x):
        self.x = x

    def __getattr__(self, name):
        if name == 'x':
            return self.x
        raise AttributeError

def test_get_ctypes_field():
    assert cffi_backend.get_ctypes_field(C(1)) == 1
    assert cffi_backend.get_ctypes_field(S(1)) == 1
    assert cffi_backend.get_ctypes_field(1) == 1
    raises(AttributeError, cffi_backend.get_ctypes_field, object())

def test_get_ctypes_type():
    assert cffi_backend.get_ctypes_type(C(1)) == ctypes.c_int
    assert cffi_backend.get_ctypes_type(S(1)) == ctypes.c_int
    assert cffi_backend.get_ctypes_type(1) == ctypes.c_int
   
