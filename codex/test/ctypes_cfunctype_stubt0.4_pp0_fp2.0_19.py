import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello"

def test_call_c_function():
    assert fun() == "Hello"

def test_call_c_function_with_args():
    @FUNTYPE
    def fun(x):
        return x+1
    assert fun(1) == 2

def test_call_c_function_with_kwargs():
    @FUNTYPE
    def fun(x=1):
        return x+1
    assert fun(x=1) == 2

def test_call_c_function_with_args_and_kwargs():
    @FUNTYPE
    def fun(x, y=1):
        return x+y
    assert fun(1, y=1) == 2

def test_call_c_function_with_args_and_kwargs_and_defaults():
    @FUNTYPE
    def fun(x, y=1, z=2):
        return x+y+z
    assert fun(1, y=1) == 4

