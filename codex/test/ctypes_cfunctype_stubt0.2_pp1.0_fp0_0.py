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
    def fun(arg1, arg2, **kwargs):
        return arg1, arg2, kwargs
    assert fun("hello", "world", foo="bar") == ("hello", "world", {"foo": "bar"})

def test_fun_with_defaults():
    @FUNTYPE
    def fun(arg1, arg2="world"):
        return arg1, arg2
    assert fun("hello") == ("hello", "world")
    assert fun("hello", "world") == ("hello", "world")


