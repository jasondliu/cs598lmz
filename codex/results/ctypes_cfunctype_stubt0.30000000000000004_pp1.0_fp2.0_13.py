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

def test_fun_with_kwarg():
    @FUNTYPE
    def fun(arg="hello"):
        return arg
    assert fun() == "hello"

def test_fun_with_kwarg_and_arg():
    @FUNTYPE
    def fun(arg, arg2="hello"):
        return arg, arg2
    assert fun("hello") == ("hello", "hello")

def test_fun_with_kwarg_and_arg_and_default():
    @FUNTYPE
    def fun(arg, arg2="hello", arg3=None):
        return arg, arg2, arg3
    assert fun("hello") == ("hello", "hello", None)

def test_fun_with_kwarg_and_arg_and_default_and_kwarg():
    @FUNTYPE
    def
