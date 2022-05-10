import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_fun():
    assert fun() == "hello"

def test_fun_with_arg():
    @FUNTYPE
    def fun(arg):
        return arg
    assert fun(1) == 1

def test_fun_with_kwarg():
    @FUNTYPE
    def fun(arg=1):
        return arg
    assert fun() == 1

def test_fun_with_kwarg_and_arg():
    @FUNTYPE
    def fun(arg, kwarg=1):
        return arg, kwarg
    assert fun(1) == (1, 1)
    assert fun(1, 2) == (1, 2)

def test_fun_with_kwarg_and_arg_and_default():
    @FUNTYPE
    def fun(arg, kwarg=1, default=2):
        return arg, kwarg, default
    assert fun(1) == (1, 1, 2)
    assert fun(1, 2) == (1, 2, 2)
