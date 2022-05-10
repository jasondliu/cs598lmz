import _struct
# Test _struct.Struct() class


def s(*args):
    return _struct.Struct(*args).pack(*args[1:])


class StructTest(unittest.TestCase):
    def test_bool(self):
        self.assertEqual(s('?', 0), b'\x00')
        self.assertEqual(s('?', 1), b'\x01')
        self.assertEqual(s('?', True), b'\x01')
        self.assertEqual(s('?', False), b'\x00')
        with self.assertRaises(TypeError):
            s('?', 'spam')

    def test_byteorder_char(self):
        self.assertEqual(s('=b', 1), b'\x01')
        self.assertEqual(s('<b', 1), b'\x01')
