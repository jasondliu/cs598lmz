import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def make_fun(f):
    """takes a function f as input and returns a function which has the same
    signature as the callback function required by unittest.TestCase.assertAlmostEqual"""
    return FUNTYPE(lambda x: f(x))

class TestCase(unittest.TestCase):
    """add some additional methods to unittest.TestCase"""

    def assertAlmostEqual(self, first, second, places=None, msg=None, delta=None,
                          fun=None):
        """Override assertAlmostEqual to accept an optional function fun.
        If fun is not None, then fun(first) and fun(second) are compared to
        within the specified tolerance. fun should be a function that takes a
        single float argument and returns a float"""
        if fun:
            first = fun(first)
            second = fun(second)
        super(TestCase, self).assertAlmostEqual(first, second, places, msg, delta)

    def assertAllEqual(self, first, second
