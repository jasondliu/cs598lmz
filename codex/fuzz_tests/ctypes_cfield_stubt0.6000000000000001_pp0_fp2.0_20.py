import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)


class CFieldTests(unittest.TestCase):

    def test_repr(self):
        self.assertEqual(repr(S.x), "<field 'x' of 'S' structures>")

    def test_get(self):
        s = S()
        self.assertEqual(s.x, 0)
        s.x = 42
        self.assertEqual(s.x, 42)

    def test_set(self):
        s = S()
        s.x = 42
        self.assertEqual(s.x, 42)

    def test_type(self):
        self.assertEqual(S.x.type, ctypes.c_int)

    def test_offset(self):
        self.assertEqual(S.x.offset, ctypes.sizeof(ctypes.c_int))

    def test_size(self):
        self.assertEqual(S.x.size, ctypes.sizeof(ctypes.c_int))

    def test_index(self):
        self.assertE
