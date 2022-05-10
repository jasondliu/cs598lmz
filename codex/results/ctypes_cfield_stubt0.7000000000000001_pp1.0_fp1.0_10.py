import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield_get_args():
    s = S(42)
    assert s.x._get_args_() == (42,)
    assert not s.x._get_kwargs_()

def test_cfield_set_args():
    s = S(42)
    s.x = 12
    assert s.x == 12

def test_cfield_repr():
    s = S(42)
    assert repr(s.x) == "c_int(42)"
