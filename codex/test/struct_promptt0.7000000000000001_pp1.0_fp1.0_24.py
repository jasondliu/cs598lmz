import _struct
# Test _struct.Struct
class TestStruct(unittest.TestCase):
    def test_struct(self):
        # struct.pack returns bytes
        self.assertEqual(_struct.pack("h", 1), b'\x01\x00')
        self.assertEqual(_struct.pack("h", 256), b'\x00\x01')

        # struct.unpack returns a tuple
        self.assertEqual(_struct.unpack("h", b'\x01\x00'), (1,))
        self.assertEqual(_struct.unpack("h", b'\x00\x01'), (256,))

