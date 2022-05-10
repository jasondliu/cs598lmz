import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S1(S):
    pass

class Test(unittest.TestCase):

    def test_subclassing(self):
        self.assertEqual(S1.x.offset, S.x.offset)
        self.assertTrue(isinstance(S1.x, ctypes.CField))

if __name__ == "__main__":
    unittest.main()
    from support import review
