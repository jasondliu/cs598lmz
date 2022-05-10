import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_fun():
    assert fun() == 1

def test_fun_with_arg():
    @FUNTYPE
    def fun(arg):
        return arg
    assert fun(1) == 1

def test_fun_with_args():
    @FUNTYPE
    def fun(arg1, arg2):
        return arg1 + arg2
    assert fun(1, 2) == 3

def test_fun_with_kwargs():
    @FUNTYPE
    def fun(arg1, arg2, kwarg1=1, kwarg2=2):
        return arg1 + arg2 + kwarg1 + kwarg2
    assert fun(1, 2, kwarg1=3, kwarg2=4) == 10

def test_fun_with_default_args():
    @FUNTYPE
    def fun(arg1, arg2, kwarg1=1, kwarg2=2):
        return arg1 + arg2 + kwarg1 + kwarg2
    assert fun(1, 2) ==
