import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Test(unittest.TestCase):
    def test_fields(self):
        self.assertEqual(S.x, S._fields_[0][1])
        self.assertEqual(S.x, S._fields_[0][1])

if __name__ == "__main__":
    unittest.main()
