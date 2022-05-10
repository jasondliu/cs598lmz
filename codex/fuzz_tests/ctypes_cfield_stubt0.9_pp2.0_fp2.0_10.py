import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

for name in ['_pack_', '_upack_', 'from_param', '_type_', '_subtype_']:
    delattr(ctypes.CField, name)

def init_int():
    import _ctypes_test
    getattr(_ctypes_test, "init_int")()

def test(typ):
    o = typ()
    o.value = 42
    assert o.value == 42
    return o

def test_S():
    assert test(S)

def test_BSTR():
    assert isinstance(test(ctypes.BSTR), unicode)

def test_WinError():
    assert test(ctypes.WinError)

def test_byref():
    class X(ctypes.Structure):
        _fields_ = [("value", ctypes.c_int)]
    x = X()
    x.value = 42
    ptr = ctypes.byref(x)
    assert type(ptr._objects) is dict
    assert x.value == ctypes.cast(ptr, ctypes
