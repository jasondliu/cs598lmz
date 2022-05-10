import _struct
# Test _struct.Struct

class TestStruct(unittest.TestCase):
    def test_struct_unpack(self):
        self.assertEqual(_struct.Struct('h').unpack('\x01\x00'), (1,))
        self.assertEqual(_struct.Struct('h').unpack('\x01\x00'), (1,))
        self.assertEqual(_struct.Struct('h').unpack('\x01\x00'), (1,))
        self.assertEqual(_struct.Struct('h').unpack('\x01\x00'), (1,))
        self.assertEqual(_struct.Struct('h').unpack('\x01\x00'), (1,))
        self.assertEqual(_struct.Struct('h').unpack('\x01\x00'), (1,))
        self.assertEqual(_struct.Struct('h').unpack('\x01\x00'), (1,))
        self.assertEqual(_struct.Struct('h').unpack('\x01\x00'), (1,))
        self.assertEqual
