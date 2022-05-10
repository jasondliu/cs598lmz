import _struct
# Test _struct.Struct

def test_struct(s, fmt, exp_data, exp_unpack, *data_args):
    assert s.__doc__ == "compiled struct"
    assert s.format == fmt
    assert s.size == _struct.calcsize(fmt)
    assert s.pack(*data_args) == exp_data
    assert s.pack_into(buffer(bytearray(s.size)), 0, *data_args) is None
    assert s.unpack(exp_data) == exp_unpack
    assert s.unpack_from(buffer(exp_data), 0) == exp_unpack

for fmt, exp_data, exp_unpack, data_args in [
        ('x', b'', (), ()),
        ('c', b'a', ('a',), ('a',)),
        ('cx', b'a\x00', ('a',), ('a',)),
        ('b', b'\x01', (1,), (1,)),
        ('b', b'\xff', (-1,), (-1,)),
        ('
