import ctypes

class S(ctypes.Structure):
    x = None
    _fields_ = [("x", S)]

class A(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

class Test_O(unittest.TestCase):
    def test(self):
        self.assertRaises(TypeError, ctypes.sizeof, S)
        self.assertRaises(TypeError, ctypes.sizeof, A, S)

    def test_from_address(self):
        with support.Checker(self) as check:
            a = A(24)
            check(a.value, 24)
            b = A.from_address(ctypes.addressof(a))
            check(repr(b), "A(x=24)")
            check(repr(b.x), "c_int(24)")
            check(a.x, 24)
            a.x = 42
            check(b.x, 42)

            a = A(24)
            b = A.from_address(ctypes.addressof(a))
           
