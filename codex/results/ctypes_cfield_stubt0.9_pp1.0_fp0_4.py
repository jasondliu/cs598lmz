import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
def test_readonly_classfield():
    # Bug #493342: accessed through class, field is writable
    assert hasattr(S.x, '__set__')
    raises(AttributeError, setattr, S.x, '_value', 5)
    raises(TypeError, S.x.__set__, None, 5)

def test_readonly_cfield_instance():
    # Bug #493342: accessed through instance, field is writable
    S1 = S()
    raises(AttributeError, setattr, S1.x, '_value', 5)
    raises(TypeError, S1.x.__set__, S1, 5)
