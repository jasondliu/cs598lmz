import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_call_c_function():
    assert fun() == "hello"

def test_call_c_function_with_arg():
    @FUNTYPE
    def fun(x):
        return x
    assert fun(42) == 42

def test_call_c_function_with_kwarg():
    @FUNTYPE
    def fun(x):
        return x
    assert fun(x=42) == 42

def test_call_c_function_with_arg_and_kwarg():
    @FUNTYPE
    def fun(x, y):
        return x + y
    assert fun(1, y=2) == 3

def test_call_c_function_with_kwargs():
    @FUNTYPE
    def fun(x, y):
        return x + y
    assert fun(1, y=2) == 3

def test_call_c_function_with_kwargs_and_kwarg():
    @FUNTYPE
    def fun(x, y):
        return x + y
    assert fun
