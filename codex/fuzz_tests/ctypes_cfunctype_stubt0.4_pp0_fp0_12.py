import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_call_function():
    assert fun() == "hello"

def test_call_function_with_arguments():
    @FUNTYPE
    def fun(a, b):
        return a + b
    assert fun(1, 2) == 3

def test_call_function_with_kwargs():
    @FUNTYPE
    def fun(a, b):
        return a + b
    assert fun(a=1, b=2) == 3

def test_call_function_with_defaults():
    @FUNTYPE
    def fun(a, b=1):
        return a + b
    assert fun(1) == 2
    assert fun(1, 2) == 3

def test_call_function_with_varargs():
    @FUNTYPE
    def fun(a, *args):
        return a + sum(args)
    assert fun(1, 2, 3) == 6

def test_call_function_with_kwargs():
    @FUNTYPE
    def fun(a, **kwargs):

