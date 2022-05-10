import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def test_fun():
    assert fun() == 42

def test_fun_callable():
    assert callable(fun)

def test_fun_callable_with_args():
    assert callable(fun, 1, 2, 3)

def test_fun_callable_with_kwargs():
    assert callable(fun, a=1, b=2, c=3)

def test_fun_callable_with_args_and_kwargs():
    assert callable(fun, 1, 2, 3, a=1, b=2, c=3)

def test_fun_callable_with_args_and_kwargs_and_starargs():
    assert callable(fun, 1, 2, 3, a=1, b=2, c=3, *(4, 5, 6))

def test_fun_callable_with_args_and_kwargs_and_starargs_and_kwargs():
    assert callable(fun, 1, 2, 3, a=1, b=2, c=3
