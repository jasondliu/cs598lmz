import _struct
# Test _struct.Struct.__repr__, see issue #20359
_struct.Struct("L").__repr__()

# Test _struct.Struct.__sizeof__
_struct.Struct("L").__sizeof__()

# Test _struct.Struct.pack_into
s = _struct.Struct("L")
buf = bytearray(4)
s.pack_into(buf, 0, 123456)

# Test _struct.Struct.unpack_from
_struct.unpack_from("L", buf, 0)

# Test _struct.Struct.iter_unpack
list(s.iter_unpack(buf))

# Test _struct.Struct.pack
_struct.pack("L", 123456)

# Test _struct.Struct.unpack
_struct.unpack("L", buf)

# Test _struct.Struct.iter_unpack
list(_struct.iter_unpack("L", buf))

# Test _struct.Struct.size
s.size == 4
