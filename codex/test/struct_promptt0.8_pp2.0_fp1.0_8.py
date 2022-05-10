import _struct
# Test _struct.Struct
t = _struct.Struct('3s3s')
t.size
t.pack(b"aa", b"bb")
t.unpack(b"aaabbb")
t.unpack(b"bbaaabbb")
t
t.format

# Test _struct.Struct.pack_into() and _struct.Struct.unpack_from()

a = bytearray(b"aaaabbbbcccc")
t.pack_into(a, 4, b"dd", b"ee")
a
t.unpack_from(a, 4)

a = array.array('b', b"aaaabbbbcccc")
t.pack_into(a, 4, b"dd", b"ee")
t.unpack_from(a, 4)
t

# Test _struct.pack() and _struct.unpack()

_struct.pack('3s3s', b"aa", b"bb")
_struct.unpack('3s3s', b"aaabbb")

