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
    def fun(a, b):
        return a + b

    assert fun(a=1, b=2) == 3

def test_fun_with_args_and_kwargs():
    @FUNTYPE
    def fun(a, b, c):
        return a + b + c

    assert fun(1, b=2, c=3) == 6

def test_fun_with_args_and_kwargs_and_defaults():
    @FUNTYPE
    def fun(a, b, c=3):
        return a + b + c

    assert fun(1, b=2) == 6

