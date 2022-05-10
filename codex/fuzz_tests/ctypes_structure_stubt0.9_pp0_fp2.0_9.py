import ctypes

class S(ctypes.Structure):
    x = None
    _fields_ = [("x", ctypes.POINTER(ctypes.c_int32))]

class TestFoo(unittest.TestCase):
    def test_foo_equals(self):
        print('hello')
        self.assertTrue(1 == 1)


if __name__ == '__main__':
    unittest.main()
