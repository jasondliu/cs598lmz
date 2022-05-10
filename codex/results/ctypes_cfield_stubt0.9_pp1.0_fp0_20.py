import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_field_except(self):
    raises(AttributeError, setattr, S.x, 'other', 0)
    raises(AttributeError, 'S.x = "string"')

if __name__ == '__main__':
    import test.support
    test.support.run_unittest(__name__)
