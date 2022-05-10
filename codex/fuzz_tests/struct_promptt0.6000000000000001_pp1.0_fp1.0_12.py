import _struct
# Test _struct.Struct.
struct = _struct.Struct("@bbc")
self.assertEqual(struct.size, 4)
self.assertEqual(struct.pack(65, 66, 67), b"ABC\x00")
self.assertEqual(struct.unpack(b"ABC\x00"), (65, 66, 67, 0))
self.assertEqual(struct.unpack(b"ABC\x00"), (65, 66, 67, 0))
# A second call to Struct() returns the same object.
self.assertEqual(_struct.Struct("@bbc"), struct)

# Test _struct.Struct.format
struct = _struct.Struct("bbc")
self.assertEqual(struct.format, "bbc")

# Test _struct.Struct.pack_into
buf = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00")
struct = _struct.Struct("@ii")
struct.pack_into(buf, 4, 2, 3)
self.assertEqual(buf, b"
