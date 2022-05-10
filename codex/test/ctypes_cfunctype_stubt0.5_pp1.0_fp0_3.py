import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_function_type():
    assert fun() == "hello"
    assert type(fun) is FUNTYPE

def test_function_type_none():
    assert FUNTYPE(None)() is None

def test_function_type_args():
    def f(*args):
        return args
    assert FUNTYPE(f)(1, 2, 3) == (1, 2, 3)

def test_function_type_kwargs():
    def f(**kwargs):
        return kwargs
    assert FUNTYPE(f)(a=1, b=2, c=3) == {"a": 1, "b": 2, "c": 3}

def test_function_type_optional():
    def f(a, b, c=3):
        return a, b, c
    assert FUNTYPE(f)(1, 2) == (1, 2, 3)
    assert FUNTYPE(f)(1, 2, 3) == (1, 2, 3)

