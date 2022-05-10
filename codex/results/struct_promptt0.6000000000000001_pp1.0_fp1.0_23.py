import _struct
# Test _struct.Struct
class StructTestCase(unittest.TestCase):
    def test_struct(self):
        with self.assertRaises(TypeError):
            _struct.Struct()
        with self.assertRaises(TypeError):
            _struct.Struct(42)
        with self.assertRaises(TypeError):
            _struct.Struct('abc', 42)
        with self.assertRaises(TypeError):
            _struct.Struct('abc', b'def', 42)
        self.assertEqual(_struct.Struct('i').size, _struct.calcsize('i'))
        self.assertEqual(_struct.Struct('i').format, 'i')
        self.assertEqual(_struct.Struct('i').pack(42), _struct.pack('i', 42))
        self.assertEqual(_struct.Struct('i').pack_into(bytearray(b'\0' * 4), 0, 42),
                         _struct.pack_into(bytearray(b'\0' * 4), 0, 'i', 42))
        self.assertEqual(_
