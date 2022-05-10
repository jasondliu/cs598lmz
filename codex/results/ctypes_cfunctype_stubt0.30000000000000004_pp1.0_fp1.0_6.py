import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_fun():
    f = fun()
    assert f() == "hello"

def test_fun_with_args():
    f = fun
    assert f() == "hello"

def test_fun_with_args_and_kwargs():
    f = fun
    assert f() == "hello"

def test_fun_with_args_and_kwargs_and_starargs():
    f = fun
    assert f() == "hello"

def test_fun_with_args_and_kwargs_and_starargs_and_starkwargs():
    f = fun
    assert f() == "hello"

def test_fun_with_args_and_kwargs_and_starargs_and_starkwargs_and_more():
    f = fun
    assert f() == "hello"

def test_fun_with_args_and_kwargs_and_starargs_and_starkwargs_and_more_and_more():
    f = fun
    assert f() == "hello"
