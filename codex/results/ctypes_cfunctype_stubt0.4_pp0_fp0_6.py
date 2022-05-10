import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def test_fun():
    assert fun() == 42

def test_fun_with_args():
    @FUNTYPE
    def fun(x):
        return x*2
    assert fun(21) == 42

def test_fun_with_kwargs():
    @FUNTYPE
    def fun(x=42):
        return x
    assert fun() == 42
    assert fun(21) == 21

def test_fun_with_kwargs_and_defaults():
    @FUNTYPE
    def fun(x=42, y=21):
        return x+y
    assert fun() == 63
    assert fun(21) == 42
    assert fun(21, 21) == 42

def test_fun_with_varargs():
    @FUNTYPE
    def fun(*args):
        return sum(args)
    assert fun() == 0
    assert fun(1) == 1
    assert fun(1, 2) == 3
    assert fun(1, 2, 3) == 6
    assert fun(1, 2, 3, 4) == 10
