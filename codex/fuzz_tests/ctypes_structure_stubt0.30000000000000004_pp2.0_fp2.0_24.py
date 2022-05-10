import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

class Test(unittest.TestCase):
    def test(self):
        s = S()
        s.x = 1
        s.y = 2
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)

        s2 = S()
        s2.x = 3
        s2.y = 4
        self.assertEqual(s2.x, 3)
        self.assertEqual(s2.y, 4)

        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)

if __name__ == "__main__":
    unittest.main()
