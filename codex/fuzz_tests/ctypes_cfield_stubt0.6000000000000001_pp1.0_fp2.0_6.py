import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Test(unittest.TestCase):
    def test_cfield(self):
        self.assertEqual(ctypes.CField.__bases__, (ctypes.Field, ctypes.c_int))
        s = S()
        self.assertEqual(s.x, 0)
        s.x = 42
        self.assertEqual(s.x, 42)
        self.assertIsInstance(s.x, ctypes.c_int)

if __name__ == "__main__":
    unittest.main()
