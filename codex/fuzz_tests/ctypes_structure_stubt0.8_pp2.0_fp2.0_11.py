import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float(1.0)
    y = ctypes.c_float(2.0)
    z = ctypes.c_float(3.0)

class StructTest(unittest.TestCase):
    def test_count(self):
        self.assertEqual(3, len(S()))
        
    def test_getitem(self):
        s = S()
        self.assertEqual(1.0, s[0])
        self.assertEqual(2.0, s[1])
        self.assertEqual(3.0, s[2])

    def test_setitem(self):
        s = S()
        s[0] = 2.0
        s[1] = 3.0
        s[2] = 4.0
        self.assertEqual(2.0, s[0])
        self.assertEqual(3.0, s[1])
        self.assertEqual(4.0, s[2])
        
    def test_iter_keys(self):
        s =
