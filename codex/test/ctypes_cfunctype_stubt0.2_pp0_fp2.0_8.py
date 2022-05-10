import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_fun():
    assert fun() == "hello"

def test_fun_with_arg():
    @FUNTYPE
    def fun(x):
        return x
    assert fun(42) == 42

def test_fun_with_kwarg():
    @FUNTYPE
    def fun(x=42):
        return x
    assert fun() == 42

def test_fun_with_kwarg_and_default():
    @FUNTYPE
    def fun(x=42):
        return x
    assert fun(x=24) == 24

def test_fun_with_kwarg_and_default_and_arg():
    @FUNTYPE
    def fun(x=42):
        return x
    assert fun(24) == 24

def test_fun_with_kwarg_and_default_and_arg_and_kwarg():
    @FUNTYPE
    def fun(x=42):
        return x
    assert fun(24, x=24) == 24

