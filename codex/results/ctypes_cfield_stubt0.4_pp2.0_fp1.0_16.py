import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CFieldTestCase(unittest.TestCase):
    def test_repr(self):
        self.assertEqual(repr(S.x), '<field x of type c_int>')

    def test_type_name(self):
        self.assertEqual(S.x.type_name, 'int')

    def test_name(self):
        self.assertEqual(S.x.name, 'x')

    def test_offset(self):
        self.assertEqual(S.x.offset, ctypes.c_int.in_dll(S, 'x').value)

    def test_index(self):
        self.assertEqual(S.x.index, 0)

    def test_size(self):
        self.assertEqual(S.x.size, ctypes.sizeof(ctypes.c_int))

    def test_get_pack_size(self):
        self.assertEqual(S.x.get_pack_size(), ctypes.sizeof(ctypes.c_int))


