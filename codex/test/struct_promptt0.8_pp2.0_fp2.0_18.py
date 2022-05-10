import _struct
# Test _struct.Struct init
# types: int
def test_struct_int_init():
    s = _struct.Struct(1)
    assert type(s) == _struct.Struct
    assert s.size == 2
    assert s.format == 'hh'
    assert s.unpack('\0\0') == (0, 0)

def test_struct_longlong_init():
    s = _struct.Struct(3)
    assert s.size == 4
    assert s.format == 'll'
    assert s.unpack('\0\0\0\0') == (0, 0)

def test_struct_uint_init():
    s = _struct.Struct(5)
    assert s.size == 4
    assert s.format == 'LL'
    assert s.unpack('\0\0\0\0') == (0, 0)

def test_struct_float_init():
    s = _struct.Struct(6)
    assert s.size == 4
    assert s.format == 'f'
