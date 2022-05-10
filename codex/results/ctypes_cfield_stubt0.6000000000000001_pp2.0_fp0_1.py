import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

@pytest.mark.parametrize('attr', dir(ctypes.CField))
def test_cfield_attrs_cannot_be_set(attr):
    s = S()
    with pytest.raises(AttributeError):
        setattr(s.x, attr, 0)

@pytest.mark.parametrize('attr', dir(ctypes.CFuncPtr))
def test_cfuncptr_attrs_cannot_be_set(attr):
    def f(*args):
        pass
    f.restype = ctypes.c_int
    with pytest.raises(AttributeError):
        setattr(f, attr, 0)
