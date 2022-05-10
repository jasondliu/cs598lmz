import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def test_fun():
    assert fun() == 42

def test_fun_call():
    assert fun.__call__() == 42

def test_fun_call_args():
    raises(TypeError, fun.__call__, 1)

def test_fun_call_kwargs():
    raises(TypeError, fun.__call__, x=1)

def test_fun_call_args_kwargs():
    raises(TypeError, fun.__call__, 1, x=1)

def test_fun_call_args_kwargs_star():
    raises(TypeError, fun.__call__, 1, x=1, *(1,))

def test_fun_call_args_kwargs_starstar():
    raises(TypeError, fun.__call__, 1, x=1, **{'x': 1})

def test_fun_call_args_kwargs_star_starstar():
    raises(TypeError, fun.__call__, 1, x=1, *(1,), **{'x
