import _struct
# Test _struct.Struct 
class TestStruct(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(_struct.Struct('i').size, 4)
        self.assertEqual(_struct.Struct('i').format, 'i')
        self.assertEqual(_struct.Struct('h').size, 2)
        self.assertEqual(_struct.Struct('h').format, 'h')


class TestStructOps(unittest.TestCase):
    def test_pack(self):
        self.assertEqual(_struct.Struct('i').pack(1), b'\x01\x00\x00\x00')
        self.assertEqual(_struct.Struct('h').pack(1), b'\x01\x00')

    def test_unpack(self):
        self.assertEqual(_struct.Struct('i').unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(_struct.Struct('h').unpack(b'\x01\x00'), (1,))


