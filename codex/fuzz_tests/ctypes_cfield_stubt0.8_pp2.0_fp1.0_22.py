import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

@unittest.skipUnless(is_cli, 'IronPython specific test')
class TestBaseField(unittest.TestCase):
    def test_type_fields(self):
        s = S()

        for t in [int, long, bool, float]:
            s.x = t(1)
            self.assertEqual(int(s.x), 1)
            self.assertEqual(type(s.x), int)

        s.x = 1
        self.assertEqual(int(s.x), 1)
        self.assertEqual(type(s.x), int)

        s.x = ctypes.c_byte(1)
        self.assertEqual(s.x, 1)

    def test_class_fields(self):
        s = S()
        s.x = "abc"

        self.assertRaises(TypeError, setattr, s, 'x', "def")
        self.assertRaises(TypeError, setattr, S, 'x', "def")

        del s.x
        self.assert
