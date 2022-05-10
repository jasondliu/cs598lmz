from _struct import Struct
s = Struct.__new__(Struct)
s.size = lambda: 1
s.format = 'x'

def test_struct_size():
    assert s.size() == 1

def test_struct_format():
    assert s.format == 'x'

def test_struct_pack():
    assert s.pack(1) == b'\x00'

def test_struct_unpack():
    assert s.unpack(b'\x00') == (0,)

def test_struct_iter_unpack():
    assert list(s.iter_unpack(b'\x00\x01')) == [(0,), (1,)]

def test_struct_unpack_from():
    assert s.unpack_from(b'\x00\x01', 1) == (1,)

def test_struct_iter_unpack_from():
    assert list(s.iter_unpack_from(b'\x00\x01\x02', 1)) == [(1,), (2,)]
