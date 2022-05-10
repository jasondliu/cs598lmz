import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

@unittest.skipUnless(hasattr(ctypes, "CField"), "requires ctypes.CField")
class TestCField(unittest.TestCase):
    def test_cfield(self):
        self.assertIs(type(S.x), ctypes.CField)

    def test_cfield_name(self):
        self.assertEqual(S.x.name, "x")

    def test_cfield_ctype(self):
        self.assertIs(S.x.ctype, ctypes.c_int)

    def test_cfield_offset(self):
        self.assertEqual(S.x.offset, ctypes.sizeof(ctypes.c_int))

    def test_cfield_size(self):
        self.assertEqual(S.x.size, ctypes.sizeof(ctypes.c_int))

    def test_cfield_index(self):
        self.assertEqual(S.x.index, 0)

    def test_cfield_pack(self):
        self.
