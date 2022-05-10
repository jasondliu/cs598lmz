import _struct
# Test _struct.Struct()
import _struct as struct

class TestStruct(unittest.TestCase):
    def test_module(self):
        self.assertTrue(hasattr(_struct, 'error'))
        self.assertTrue(hasattr(_struct, 'pack'))
        self.assertTrue(hasattr(_struct, 'unpack'))
        self.assertTrue(hasattr(_struct, 'calcsize'))
        self.assertTrue(hasattr(_struct, 'Struct'))

    def test_error(self):
        self.assertTrue(issubclass(_struct.error, Exception))

    def test_pack(self):
        self.assertEqual(_struct.pack('hhl', 1, 2, 3), b'\x01\x00\x02\x00\x00\x00\x00\x03')

    def test_unpack(self):
        self.assertEqual(_struct.unpack('hhl', b'\x01\x00\x02\x00\x00\x00\x00\x03'), (1, 2, 3))


