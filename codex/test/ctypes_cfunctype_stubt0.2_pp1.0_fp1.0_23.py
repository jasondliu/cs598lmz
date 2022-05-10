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
    assert fun("hello") == "hello"

def test_fun_with_args():
    @FUNTYPE
    def fun(arg1, arg2):
        return arg1, arg2
    assert fun("hello", "world") == ("hello", "world")

def test_fun_with_kwargs():
    @FUNTYPE
    def fun(arg1, arg2, arg3=None):
        return arg1, arg2, arg3
    assert fun("hello", "world", arg3="!") == ("hello", "world", "!")

def test_fun_with_kwargs_and_defaults():
    @FUNTYPE
    def fun(arg1, arg2, arg3=None, arg4=None):
        return arg1, arg2, arg3, arg4
