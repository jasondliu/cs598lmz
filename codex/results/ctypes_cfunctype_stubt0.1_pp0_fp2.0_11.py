import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_fun():
    assert fun() == 1

def test_fun_with_args():
    @FUNTYPE
    def fun(a, b):
        return a + b
    assert fun(1, 2) == 3

def test_fun_with_kwargs():
    @FUNTYPE
    def fun(a, b):
        return a + b
    assert fun(a=1, b=2) == 3

def test_fun_with_defaults():
    @FUNTYPE
    def fun(a, b=2):
        return a + b
    assert fun(1) == 3
    assert fun(1, 2) == 3
    assert fun(1, b=2) == 3

def test_fun_with_varargs():
    @FUNTYPE
    def fun(*args):
        return sum(args)
    assert fun(1, 2, 3) == 6

def test_fun_with_varkwargs():
    @FUNTYPE
    def fun(**kwargs):
        return sum(kwargs.values())
