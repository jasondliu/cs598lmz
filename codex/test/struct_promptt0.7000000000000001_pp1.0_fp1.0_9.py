import _struct
# Test _struct.Struct
class TestStruct(unittest.TestCase):

    def test_basics(self):
        with self.assertRaises(TypeError):
            _struct.Struct()
        with self.assertRaises(TypeError):
            _struct.Struct(42, 42)
        with self.assertRaises(TypeError):
            _struct.Struct('abc%c' % 0)
        with self.assertRaises(TypeError):
            _struct.Struct('abc%c' % ('x' * 500))
        with self.assertRaises(TypeError):
            _struct.Struct('abc%c' % ('x' * (sys.maxsize + 1)))

    def test_bool(self):
        # Issue #22755: bool type was not supported by '?' format
        with self.assertRaises(TypeError):
            _struct.Struct('?').pack(b'abc')
