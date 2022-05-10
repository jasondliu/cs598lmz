import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    print "CField:", ctypes.CField
    assert issubclass(ctypes.CField, ctypes.Field)
    print "CField.__init__:", S.x.__init__
    assert S.x.__init__ == ctypes.Field.__init__
    print "CField.from_param:", ctypes.CField.from_param
    assert ctypes.CField.from_param != ctypes.Field.from_param
