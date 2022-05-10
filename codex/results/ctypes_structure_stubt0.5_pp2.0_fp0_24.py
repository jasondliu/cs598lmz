import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_float()
    z = ctypes.c_char()

class Test(unittest.TestCase):
    def test_first(self):
        s = S()
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0.0)
        self.assertEqual(s.z, '\0')

if __name__ == "__main__":
    unittest.main()
