import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CFieldTest(unittest.TestCase):
    def test_from_param(self):
        self.assertEqual(ctypes.CField.from_param(S.x), S.x)
        self.assertEqual(ctypes.CField.from_param(S.x), S.x)
        self.assertEqual(ctypes.CField.from_param(S.x), S.x)
        self.assertEqual(ctypes.CField.from_param(S.x), S.x)
        self.assertEqual(ctypes.CField.from_param(S.x), S.x)
        self.assertEqual(ctypes.CField.from_param(S.x), S.x)
        self.assertEqual(ctypes.CField.from_param(S.x), S.x)
        self.assertEqual(ctypes.CField.from_param(S.x), S.x)

    def test_from_address(self):
        self.assertEqual(ctypes.
