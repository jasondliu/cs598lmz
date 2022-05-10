import _struct
# Test _struct.Struct()
from test import test_support

# Test _struct.Struct()

def test_struct_type():
    st = _struct.Struct('i')
    assert isinstance(st, type)

def test_struct_new():
    st = _struct.Struct('i')
    assert isinstance(st, type)
    s = st.__new__(st)
    assert isinstance(s, _struct.Struct)
    assert s.size == _struct.calcsize('i')
    assert s.format == 'i'

def test_struct_init():
    st = _struct.Struct('i')
    s = st()
    assert isinstance(s, _struct.Struct)
    assert s.size == _struct.calcsize('i')
    assert s.format == 'i'

def test_struct_pack_unpack():
    st = _struct.Struct('i')
    s = st()
    for x in range(-5, 6):
        s.pack(x)
        assert s.unpack(s.get_buffer())[
