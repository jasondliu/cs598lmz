import _struct
# Test _struct.Struct

def test_struct_pack():
    assert _struct.Struct('i').pack(1) == b'\x01\x00\x00\x00'


def test_struct_unpack():
    assert _struct.Struct('i').unpack(b'\x01\x00\x00\x00') == (1,)


def test_struct_pack_into():
    buf = array.array('b', b'\x00' * 4)
    _struct.Struct('i').pack_into(buf, 0, 1)
    assert buf == array.array('b', b'\x01\x00\x00\x00')


def test_struct_unpack_from():
    buf = array.array('b', b'\x01\x00\x00\x00')
    assert _struct.Struct('i').unpack_from(buf, 0) == (1,)
