import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_fun():
    assert fun() == "hello"

def test_fun_with_args():
    @FUNTYPE
    def fun(a, b):
        return a + b
    assert fun(1, 2) == 3

def test_fun_with_kwargs():
    @FUNTYPE
    def fun(a, b, c=3):
        return a + b + c
    assert fun(1, 2) == 6
    assert fun(1, 2, c=4) == 7

def test_fun_with_defaults():
    @FUNTYPE
    def fun(a, b, c=3):
        return a + b + c
    assert fun(1, 2) == 6
    assert fun(1, 2, c=4) == 7

def test_fun_with_varargs():
    @FUNTYPE
    def fun(a, b, *args):
        return a + b + sum(args)
    assert fun(1, 2, 3, 4) == 10

def test_fun_with_
