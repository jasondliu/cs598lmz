import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    assert isinstance(S.x, ctypes.CField)
    assert S.x.name == 'x'
    assert S.x.type == ctypes.c_int
    assert S.x.offset == 0
    assert S.x.size == ctypes.sizeof(ctypes.c_int)
    assert S.x.index == 0
    assert S.x.pack == 1
    assert S.x.bitsize == 0
    assert S.x.bitoffset == 0
    assert S.x.cname == 'x'
    assert S.x.ctype == ctypes.c_int
    assert S.x.is_array == False
    assert S.x.is_pointer == False
    assert S.x.is_volatile == False
    assert S.x.is_bitfield == False
    assert S.x.is_static_array == False
    assert S.x.is_variable_array == False
    assert S.x.is_nested_struct == False
    assert S.x.is
