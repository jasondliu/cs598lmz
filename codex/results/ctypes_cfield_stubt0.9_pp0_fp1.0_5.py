import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Test(unittest.TestCase):
    def test_gt(self):
        s = S()
        self.assertEqual(0 > s, NotImplementedError)

if __name__ == '__main__':
    unittest.main()
