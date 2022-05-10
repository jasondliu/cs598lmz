import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "foo"

def test_fun():
    assert fun() == "foo"

def test_fun_with_arg():
    assert fun(1) == "foo"

def test_fun_with_kwarg():
    assert fun(x=1) == "foo"

def test_fun_with_args_kwargs():
    assert fun(1, x=1) == "foo"

def test_fun_with_args_kwargs_star():
    assert fun(1, x=1, *(2, 3)) == "foo"

def test_fun_with_args_kwargs_star_star():
    assert fun(1, x=1, *(2, 3), **{'y': 1}) == "foo"

def test_fun_with_args_kwargs_star_star_2():
    assert fun(1, x=1, *(2, 3), y=1) == "foo"

def test_fun_with_args_kwargs_star_star_3():
    assert fun(1, x=1
