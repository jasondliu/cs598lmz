import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "fun"

def test_fun():
    assert fun() == "fun"

def test_fun_with_args():
    @FUNTYPE
    def fun(x, y):
        return x + y
    assert fun(1, 2) == 3

def test_fun_with_kwargs():
    @FUNTYPE
    def fun(x, y, z=3):
        return x + y + z
    assert fun(1, 2) == 6
    assert fun(1, 2, 4) == 7

def test_fun_with_starargs():
    @FUNTYPE
    def fun(x, y, *args):
        return x + y + sum(args)
    assert fun(1, 2) == 3
    assert fun(1, 2, 3) == 6
    assert fun(1, 2, 3, 4) == 10

def test_fun_with_starstarargs():
    @FUNTYPE
    def fun(x, y, *args, **kwargs):
        return x + y + sum(args) + sum(kwargs.
