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
    def fun(arg1, arg2):
        return arg1, arg2
    assert fun(arg2="world", arg1="hello") == ("hello", "world")

def test_fun_with_default_kwargs():
    @FUNTYPE
    def fun(arg1, arg2="world"):
        return arg1, arg2
    assert fun("hello") == ("hello", "world")

