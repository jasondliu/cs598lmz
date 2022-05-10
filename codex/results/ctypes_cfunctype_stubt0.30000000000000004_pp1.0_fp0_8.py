import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_fun():
    assert fun() == "hello"

def test_fun_with_arg():
    assert fun(1) == "hello"

def test_fun_with_kwarg():
    assert fun(a=1) == "hello"

def test_fun_with_kwargs():
    assert fun(a=1, b=2) == "hello"

def test_fun_with_args_and_kwargs():
    assert fun(1, 2, a=1, b=2) == "hello"

def test_fun_with_args_and_kwargs_and_starargs():
    assert fun(1, 2, a=1, b=2, *(3, 4)) == "hello"

def test_fun_with_args_and_kwargs_and_starargs_and_kwargs():
    assert fun(1, 2, a=1, b=2, *(3, 4), **{"c": 5, "d": 6}) == "hello"

def test_fun_with_
