import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_c_field():
    f = ctypes.CField('a', ctypes.c_int, 0)
    assert f.name == 'a'
    assert f.offset == 0
    assert f.ctype == ctypes.c_int
    assert f.size == ctypes.sizeof(ctypes.c_int)
    assert f.get_packing() == 0
    assert f.get_name() == 'a'
    assert f.get_offset() == 0
    assert f.get_size() == ctypes.sizeof(ctypes.c_int)
    assert f.get_type() == ctypes.c_int
    assert f.get_flags() == 0
    assert f.get_alignment() == ctypes.alignment(ctypes.c_int)
    assert f.get_pack_for_pointer() == 0
    assert f.get_pack_for_struct() == 0
    assert f.get_pack_for_field() == 0
    assert f.get_pack_for_value() == 0
    assert f
