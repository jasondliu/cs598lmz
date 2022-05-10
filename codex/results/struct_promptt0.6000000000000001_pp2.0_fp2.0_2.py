import _struct
# Test _struct.Struct
class StructTest(unittest.TestCase):
    def test_unpack(self):
        self.assertEqual(_struct.unpack('@i', b'\x01\x00\x00\x00'),
                         (1,))
        self.assertEqual(_struct.unpack('<i', b'\x00\x00\x00\x01'),
                         (1,))
        self.assertEqual(_struct.unpack('>i', b'\x01\x00\x00\x00'),
                         (1,))
        self.assertEqual(_struct.unpack('@q', b'\x01\x00\x00\x00'
                                             b'\x00\x00\x00\x00'),
                         (1,))
        self.assertEqual(_struct.unpack('<q', b'\x00\x00\x00\x00'
                                             b'\x00\x00\x00\x01'),
                         (1,))
        self.assertEqual(_struct.un
