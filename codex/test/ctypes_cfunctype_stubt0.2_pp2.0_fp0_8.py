import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_call_function():
    assert fun() == "hello"

def test_call_function_with_arg():
    def fun(a):
        return a
    assert fun(1) == 1

def test_call_function_with_kwargs():
    def fun(a, b=1):
        return a, b
    assert fun(1, b=2) == (1, 2)

def test_call_function_with_varargs():
    def fun(*args):
        return args
    assert fun(1, 2, 3) == (1, 2, 3)

def test_call_function_with_kwargs_and_varargs():
    def fun(*args, **kwargs):
        return args, kwargs
    assert fun(1, 2, 3, a=4, b=5) == ((1, 2, 3), {'a': 4, 'b': 5})

