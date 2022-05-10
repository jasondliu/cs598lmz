import _struct
# Test _struct.Struct
class test_Struct(unittest.TestCase):
    def test_simple_pack(self):
        self.assertEqual(_struct.pack('', ()), '')
        self.assertEqual(_struct.pack('@', ()), '')
        self.assertEqual(_struct.pack('@i', (1,)), '\x01\x00\x00\x00')
        self.assertEqual(_struct.pack('@2i', (1,2)), '\x01\x00\x00\x00\x02\x00\x00\x00')
        self.assertRaises(struct.error, _struct.pack, '@2i', (1,))

    def test_simple_unpack(self):
        self.assertEqual(_struct.unpack('', ''), ())
        self.assertEqual(_struct.unpack('@', ''), ())
        self.assertEqual(_struct.unpack('@i', '\x01\x00\x00\x00'), (1,))
        self.assertEqual(_struct.
