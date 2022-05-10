import _struct
# Test _struct.Struct
class StructTest(unittest.TestCase):
    def test_struct(self):
        with self.assertRaises(TypeError):
            _struct.Struct('i')
        with self.assertRaises(TypeError):
            _struct.Struct(b'i')
        with self.assertRaises(TypeError):
            _struct.Struct(b'i', b'i')
        with self.assertRaises(TypeError):
            _struct.Struct('i', b'i')
        with self.assertRaises(TypeError):
            _struct.Struct('i', 'i', b'i')
        with self.assertRaises(TypeError):
            _struct.Struct('i', 'i', 'i', b'i')
        with self.assertRaises(TypeError):
            _struct.Struct('i', 'i', 'i', 'i', b'i')
        with self.assertRaises(TypeError):
            _struct.Struct('i', 'i', 'i', 'i', 'i', b'i')
