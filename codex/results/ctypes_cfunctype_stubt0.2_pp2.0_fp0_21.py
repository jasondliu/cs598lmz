import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def test_fun():
    assert fun() == 42

def test_fun_callable():
    assert callable(fun)

def test_fun_call():
    assert fun() == 42

def test_fun_call_args():
    raises(TypeError, fun, 1)

def test_fun_call_kwargs():
    raises(TypeError, fun, x=1)

def test_fun_call_args_kwargs():
    raises(TypeError, fun, 1, x=1)

def test_fun_call_args_kwargs_star():
    raises(TypeError, fun, 1, x=1, *(1,))

def test_fun_call_args_kwargs_starstar():
    raises(TypeError, fun, 1, x=1, **{'x':1})

def test_fun_call_args_kwargs_star_starstar():
    raises(TypeError, fun, 1, x=1, *(1,), **{'x':1})

def test_fun_
