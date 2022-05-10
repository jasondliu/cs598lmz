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

def test_fun_with_args():
    @FUNTYPE
    def fun(arg1, arg2):
        return arg1, arg2
    assert fun(1, 2) == (1, 2)

def test_fun_with_kwargs():
    @FUNTYPE
    def fun(arg1, arg2, arg3=3):
        return arg1, arg2, arg3
    assert fun(1, 2) == (1, 2, 3)
    assert fun(1, 2, 3) == (1, 2, 3)
    assert fun(1, 2, arg3=3) == (1, 2, 3)

def test_fun_with_starargs():
    @FUNTYPE
    def fun(arg1, arg2, *args):
        return arg1, arg2, args
    assert fun(
