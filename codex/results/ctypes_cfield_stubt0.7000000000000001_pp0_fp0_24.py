import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CSimpleType = type(ctypes.c_int)

def test_CField():
    assert issubclass(ctypes.CField, ctypes.CSimpleType)
    assert issubclass(ctypes.c_int, ctypes.CSimpleType)

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

def test_field_structure_union():
    assert ctypes.sizeof(S) == ctypes.sizeof(ctypes.c_int)*2
    assert S.x.offset == 0
    assert S.y.offset == ctypes.sizeof(ctypes.c_int)
    assert S.x.size == ctypes.sizeof(ctypes.c_int)
    assert S.y.size == ctypes.sizeof(ctypes.c_int)

if __name__ == "__main__":
    test_CField()
    test_field_structure_union()
