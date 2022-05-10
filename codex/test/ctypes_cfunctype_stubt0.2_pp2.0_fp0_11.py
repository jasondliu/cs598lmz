import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_fun():
    assert fun() == "hello"

def test_fun_with_arg():
    @FUNTYPE
    def fun(a):
        return a
    assert fun(1) == 1

def test_fun_with_args():
    @FUNTYPE
    def fun(a, b):
        return a, b
    assert fun(1, 2) == (1, 2)

def test_fun_with_kwargs():
    @FUNTYPE
    def fun(a, b=2):
        return a, b
    assert fun(1) == (1, 2)
    assert fun(1, 3) == (1, 3)

def test_fun_with_kwargs_and_args():
    @FUNTYPE
    def fun(a, b=2, *args):
        return a, b, args
    assert fun(1) == (1, 2, ())
    assert fun(1, 3) == (1, 3, ())
