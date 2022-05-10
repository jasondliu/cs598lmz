import ctypes

class S(ctypes.Structure):
    x = (ctypes.c_int16)
    y = (ctypes.c_int32)

class S2(ctypes.Structure):
    pass

S2._fields_ = [('x', ctypes.c_int16), ('y', S)]

if __name__ == "__main__":
    import unittest
    import sys

    def do(fn, x):
        fn(x)
        return fn.restype._type_
    def check(fn, x, y):
        assert do(fn, x) is y

    class Test(unittest.TestCase):
        def test(self):
            f = ctypes.CFUNCTYPE(S)
            check(f, 1.2, ctypes.c_int16)

            f = ctypes.CFUNCTYPE(S, ctypes.c_int)
            check(f, 1.2, ctypes.c_int)

            f = ctypes.CFUNCTYPE(S, ctypes.c_int, ctypes.c_double)
            check(
