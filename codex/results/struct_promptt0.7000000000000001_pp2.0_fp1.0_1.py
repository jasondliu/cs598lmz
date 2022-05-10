import _struct
# Test _struct.Struct.
self.assertEqual(_struct.Struct('i').pack(1), b'\x01\x00\x00\x00')
self.assertEqual(_struct.Struct('b').pack(1), b'\x01')
# Test pack_into
buf = bytearray(b'\x00' * 4)
_struct.pack_into('i', buf, 0, 1)
self.assertEqual(buf, b'\x01\x00\x00\x00')
# Test unpack_from
self.assertEqual(_struct.unpack_from('i', b'\x01\x00\x00\x00'), (1,))
# Test iter_unpack
buf = b'\x01\x00\x00\x00\x02\x00\x00\x00'
self.assertEqual(list(_struct.Struct('i').iter_unpack(buf)), [1, 2])
# Test Struct.format
self.assertEqual(_struct.Struct('<i').format, '<i')
self.assertE
