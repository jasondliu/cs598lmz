import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()

    def __init__(self, value):
        self.x = value

    def __repr__(self):
        return '<S %d>' % self.x

    def __int__(self):
        return self.x

class PyTest(unittest.TestCase):
    def test_structure(self):
        s = S(10)
        self.assertEqual(s.x, 10)
        self.assertEqual(int(s), 10)
        self.assertEqual(repr(s), '<S 10>')
        self.assertEqual('<S %d>' % s, '<S 10>')
        self.assertEqual('<S %d>' % (s.x,), '<S 10>')

        self.assertEqual(s.x + 1, 11)
        self.assertEqual(s.x + 1 == 11, True)
        self.assertEqual(s.x + 1 != 11, False)

        self.assertEqual(s.x
