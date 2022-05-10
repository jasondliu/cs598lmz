import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_call_function():
    assert fun() == "hello"

def test_call_function_with_arg():
    @FUNTYPE
    def fun(x):
        return x
    assert fun(42) == 42

def test_call_function_with_kwarg():
    @FUNTYPE
    def fun(x=42):
        return x
    assert fun() == 42

def test_call_function_with_kwarg_and_arg():
    @FUNTYPE
    def fun(x, y=42):
        return x + y
    assert fun(1) == 43

def test_call_function_with_kwarg_and_arg_and_kwarg():
    @FUNTYPE
    def fun(x, y=42, z=1):
        return x + y + z
    assert fun(1, z=2) == 45

def test_call_function_with_kwarg_and_arg_and_kwarg_and_arg():
    @FUNTYPE
    def fun(x, y=42
