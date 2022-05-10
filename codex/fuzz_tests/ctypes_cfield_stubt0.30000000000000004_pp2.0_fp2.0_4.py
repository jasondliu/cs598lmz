import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Test(unittest.TestCase):
    def test_c_type(self):
        self.assertEqual(ctypes.c_int, ctypes.CField.__type__)
        self.assertEqual(ctypes.c_int, S.x.__type__)
        self.assertEqual(ctypes.c_int, S.x.type)

    def test_c_name(self):
        self.assertEqual("c_int", ctypes.CField.__name__)
        self.assertEqual("x", S.x.__name__)
        self.assertEqual("x", S.x.name)

    def test_c_offset(self):
        self.assertEqual(0, S.x.offset)

    def test_c_size(self):
        self.assertEqual(4, S.x.size)

    def test_c_index(self):
        self.assertEqual(0, S.x.index)

    def test_c_pack(self):
        self.
