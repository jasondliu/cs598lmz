import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)
class PYFUN(ctypes.c_int):
    def __init__(self, f):
        super(PYFUN, self).__init__()
        self.f = f
        self._as_parameter_ = f
def test_param_callback(i, func):
    assert callable(func)
    return func(i)

@FUNTYPE
def c_f(i):
    return i

@PYFUN
def p_f(i):
    return i

c_res = test_param_callback(3, c_f)
assert c_res == 3

p_res = test_param_callback(3, p_f)
assert p_res == 3

# issue #14
@FUNTYPE
def c_f_error(i):
    return i/0

class TestError(Exception):
    def __init__(self):
        Exception.__init__(self, "TestError")

@PYFUN
def p_f_error(i):
    raise TestError


