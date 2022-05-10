import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_fun():
    assert fun() == "hello"

def test_fun_callable():
    assert callable(fun)

def test_fun_call():
    assert fun() == "hello"

def test_fun_call_with_args():
    assert fun(1, 2, 3) == "hello"

def test_fun_call_with_kwargs():
    assert fun(a=1, b=2, c=3) == "hello"

def test_fun_call_with_args_and_kwargs():
    assert fun(1, 2, 3, a=1, b=2, c=3) == "hello"

def test_fun_call_with_args_and_kwargs_and_starargs():
    assert fun(1, 2, 3, a=1, b=2, c=3, *(4, 5, 6)) == "hello"

def test_fun_call_with_args_and_kwargs_and_starargs_and_kwargs():
    assert fun
