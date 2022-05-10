import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long(3)
    _fields_ = [('x', ctypes.c_long), ('y', ctypes.c_long)]

class Test(unittest.TestCase):
    def test_set(self):
        # this test case is different from TestSetValues
        s = S()
        s.y = 5
        self.assertRaises(TypeError, S, [], s)

if __name__ == '__main__':
    unittest.main()
