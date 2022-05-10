import _struct
# Test _struct.Struct with the native byte order
s = _struct.Struct(">I")
self.assertEqual(s.size, _struct.calcsize(">I"))
self.assertEqual(s.pack(0x01020304), b"\x01\x02\x03\x04")
self.assertEqual(s.unpack(b"\x01\x02\x03\x04"), (0x01020304,))
# Test _struct.Struct with a non-native byte order
s = _struct.Struct("<I")
self.assertEqual(s.size, _struct.calcsize("<I"))
self.assertEqual(s.pack(0x01020304), b"\x04\x03\x02\x01")
self.assertEqual(s.unpack(b"\x04\x03\x02\x01"), (0x01020304,))
# Test _struct.Struct with a standard size
s = _struct.Struct("P")
self.assertEqual(s.size, _struct.calcsize("
