import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

class TestJit(unittest.TestCase):
    def test_basic_jit(self):
        py.test.skip("works, but not on all platforms")
        def f():
            return 1
        f_jit = jit(f)
        assert f_jit() == 1

    def test_jit_with_args(self):
        py.test.skip("works, but not on all platforms")
        def f(x):
            return x
        f_jit = jit(f)
        assert f_jit(1) == 1

    def test_jit_with_kwargs(self):
        py.test.skip("works, but not on all platforms")
        def f(x, y=2):
            return x + y
        f_jit = jit(f)
        assert f_jit(1) == 3
        assert f_jit(1, y=3) == 4

    def test_jit_with_kwargs_and_defaults(self):
        py.test.skip("works, but not on all platforms")

