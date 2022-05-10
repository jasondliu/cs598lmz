import _struct
# Test _struct.Struct

def test_struct_docstring():
    struct = _struct.Struct('i')
    assert struct.__doc__ == 'Compiled struct object'

def test_struct_size():
    struct = _struct.Struct('i')
    assert struct.size == _struct.calcsize('i')

def test_struct_pack():
    struct = _struct.Struct('i')
    assert struct.pack(42) == _struct.pack('i', 42)

def test_struct_pack_iterable():
    struct = _struct.Struct('ii')
    assert struct.pack(1, 2) == _struct.pack('ii', 1, 2)

def test_struct_unpack():
    struct = _struct.Struct('i')
    assert struct.unpack(_struct.pack('i', 42)) == (42,)

def test_struct_unpack_buffer():
    struct = _struct.Struct('i')
    assert struct.unpack_from(_struct.pack('i', 42)) == (42,)

def test_struct_unpack_from_offset
