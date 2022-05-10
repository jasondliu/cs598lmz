import _struct
# Test _struct.Struct.unpack_from(buf, offset)

def test(s, buf, offset):
    print(s.unpack_from(buf, offset))

s = _struct.Struct('=BB')
test(s, b'\x01\x02\x03', 0)
test(s, b'\x01\x02\x03', 1)
test(s, b'\x01\x02', 0)
test(s, b'\x01\x02', 1)
