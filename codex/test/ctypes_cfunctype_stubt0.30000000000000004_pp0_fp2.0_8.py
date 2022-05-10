import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def test_call_c_function():
    assert fun() == 42

def test_call_c_function_with_args():
    @FUNTYPE
    def fun(a, b):
        return a + b
    assert fun(1, 2) == 3

def test_call_c_function_with_kwargs():
    @FUNTYPE
    def fun(a, b):
        return a + b
    assert fun(a=1, b=2) == 3

def test_call_c_function_with_args_and_kwargs():
    @FUNTYPE
    def fun(a, b):
        return a + b
    assert fun(1, b=2) == 3

def test_call_c_function_with_kwargs_and_args():
    @FUNTYPE
    def fun(a, b):
        return a + b
    assert fun(b=2, a=1) == 3

