import _struct
# Test _struct.Struct.
print(_struct.Struct("bhi").size)
# Test _struct.Struct.__repr__.
print(_struct.Struct("bhi").__repr__())
# Test _struct.Struct.pack.
print(_struct.Struct("bhi").pack(1, 2, 3))
# Test _struct.Struct.unpack.
print(_struct.Struct("bhi").unpack(b"\x01\x02\x00\x00\x00\x03\x00"))
# Test _struct.Struct.iter_unpack.
print(list(_struct.Struct("bhi").iter_unpack(b"\x01\x02\x00\x00\x00\x03\x00")))
# Test _struct.Struct.unpack_from.
print(_struct.Struct("bhi").unpack_from(b"\x01\x02\x00\x00\x00\x03\x00"))
# Test _struct.Struct.iter_unpack_from.
