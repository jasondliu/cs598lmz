import _struct
# Test _struct.Struct.pack_into
def test_pack_into():
    s = _struct.Struct('i')
    buf = array.array('c', b'1234567890123456')
    s.pack_into(buf, 0, 42)
    assert buf == array.array('c', b'*'.ljust(16, b'\x00'))
    s.pack_into(buf, 0, 2147483647)
    assert buf == array.array('c', b'\x7f\xff\xff\xff' + b'\x00' * 12)
    s.pack_into(buf, 0, -2147483647)
    assert buf == array.array('c', b'\x81\xff\xff\xff' + b'\x00' * 12)
    s.pack_into(buf, 0, -2147483648)
    assert buf == array.array('c', b'\x80\x00\x00\x00' + b'\x00' * 12)
