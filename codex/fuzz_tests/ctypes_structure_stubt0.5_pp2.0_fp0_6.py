import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()

class Test(unittest.TestCase):
    def test_byref(self):
        s = S()
        self.assertRaises(TypeError, ctypes.byref, s.x)

if __name__ == "__main__":
    unittest.main()
