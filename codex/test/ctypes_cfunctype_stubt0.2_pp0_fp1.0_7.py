import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_call_function():
    assert fun() == "hello"

def test_call_function_with_args():
    @FUNTYPE
    def fun(a, b):
        return a + b
    assert fun(1, 2) == 3

def test_call_function_with_kwargs():
    @FUNTYPE
    def fun(a, b):
        return a + b
    assert fun(a=1, b=2) == 3

def test_call_function_with_args_and_kwargs():
    @FUNTYPE
    def fun(a, b):
        return a + b
    assert fun(1, b=2) == 3

def test_call_function_with_defaults():
    @FUNTYPE
    def fun(a, b=2):
        return a + b
    assert fun(1) == 3

def test_call_function_with_args_and_defaults():
    @FUNTYPE
    def fun(a, b=2):
        return a + b
