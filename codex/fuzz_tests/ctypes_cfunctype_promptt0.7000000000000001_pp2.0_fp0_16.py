import ctypes
# Test ctypes.CFUNCTYPE
def func1(x):
    "Test function that returns its argument"
    return x

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
cmp_func = CMPFUNC(func1)

cmp_func.__name__ = 'cmp_func'

class TestCase(unittest.TestCase):

    def test_basic(self):
        self.failUnlessEqual(cmp_func(3), 3)
        self.failUnlessEqual(cmp_func(42), 42)

if __name__ == '__main__':
    unittest.main()
