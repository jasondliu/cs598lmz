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
    def fun(arg, arg2=1):
        return arg, arg2
    assert fun(2) == (2, 1)

def test_fun_with_kwarg_and_arg_and_kwarg():
    @FUNTYPE
    def fun(arg, arg2=1, arg3=2):
        return arg, arg2, arg3
    assert fun(2) == (2, 1, 2)
    assert fun(2, 3) == (2, 3, 2)
    assert fun(2, 3, 4) == (2, 3, 4)

