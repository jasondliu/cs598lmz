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

def test_call_function_with_keyword_arguments():
    @FUNTYPE
    def fun(a, b):
        return a + b
    assert fun(a=1, b=2) == 3

def test_call_function_with_default_arguments():
    @FUNTYPE
    def fun(a, b=2):
        return a + b
    assert fun(1) == 3
    assert fun(1, b=3) == 4

def test_call_function_with_varargs():
    @FUNTYPE
    def fun(*args):
        return sum(args)
    assert fun(1, 2, 3) == 6

