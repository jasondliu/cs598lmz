import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    assert isinstance(S.x, ctypes.CField)
    assert S.x.__name__ == 'x'
    assert S.x.__doc__ == None
    assert S.x.__module__ == 'ctypes'
    assert S.x.__dict__ is None
    assert S.x.type is ctypes.c_int
    assert S.x.offset == 0
    assert S.x.size == 4
    assert S.x.index == 0
    assert S.x.pack == 1
    assert S.x.bitsize == 32
    assert S.x.bitoffset == 0
    assert S.x.readonly == False
    assert S.x.name == 'x'
    assert S.x.type_name == 'c_int'
    assert S.x.field_name == 'x'
    assert S.x.field_type == ctypes.c_int
    assert S.x.field_size == 4
    assert S.x.field_offset == 0
    assert S.x.
