import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_c_function_call():
    assert fun() == "hello"

def test_c_function_call_with_args():
    @FUNTYPE
    def fun(a):
        return a
    assert fun(1) == 1
    assert fun(2.0) == 2.0
    assert fun("hello") == "hello"

def test_c_function_call_with_kwargs():
    @FUNTYPE
    def fun(a, b=1):
        return a + b
    assert fun(1) == 2
    assert fun(1, b=2) == 3
    assert fun(1, 2) == 3

def test_c_function_call_with_args_and_kwargs():
    @FUNTYPE
    def fun(a, b, c=1):
        return a + b + c
    assert fun(1, 2) == 4
    assert fun(1, 2, c=3) == 6
    assert fun(1, 2, 3) == 6

def test_c_function_call
