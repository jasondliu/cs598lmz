import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)

def empty_sum():
    return 0.0

class Test_Integrate_Std(unittest.TestCase):
    def test_empty(self):
        res = integrate(empty_sum, 1, 10, 100)
        self.assertEqual(res, 0)

    def test_const(self):
        def f(x):
            return 1
        res = integrate(f, 1, 10, 100)
        self.assertEqual(res, 9)

    def test_linear(self):
        def f(x):
            return x
        res = integrate(f, 1, 10, 100)
        self.assertEqual(res, 55)

    def test_cubic(self):
        def f(x):
            return x**3
        res = integrate(f, 1, 10, 100)
        self.assertEqual(res, 3025)

    def test_exp(self):
        def f(x):
            return exp(x)
        res = integrate(f, 1, 10, 100)
