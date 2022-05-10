import _struct
# Test _struct.Struct


class StructTest(unittest.TestCase):

    def test_unpack(self):
        self.assertEqual(_struct.unpack("<2s", b"AB"), (b"AB",))
        self.assertEqual(_struct.unpack("<2s", memoryview(b"AB")), (b"AB",))
        self.assertEqual(_struct.unpack("<2s", bytearray(b"AB")), (b"AB",))
        self.assertEqual(_struct.unpack("<2s", bytearray(b"AB"), 0), (b"AB",))
        self.assertEqual(_struct.unpack("<2s", bytearray(b"ABC"), 0), (b"AB",))
        self.assertEqual(_struct.unpack("<2s", bytearray(b"ABC"), 1), (b"BC",))
