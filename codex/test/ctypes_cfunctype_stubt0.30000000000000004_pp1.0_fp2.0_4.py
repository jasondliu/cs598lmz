import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def test_fun(space):
    w_fun = space.wrap(fun)
    assert space.unwrap(space.call_function(w_fun)) == 42

def test_fun_call_args(space):
    w_fun = space.wrap(fun)
    assert space.unwrap(space.call_function(w_fun, space.wrap(1), space.wrap(2))) == 42

def test_fun_call_kwargs(space):
    w_fun = space.wrap(fun)
    assert space.unwrap(space.call_function(w_fun, w_x=space.wrap(1), w_y=space.wrap(2))) == 42

def test_fun_call_args_kwargs(space):
    w_fun = space.wrap(fun)
    assert space.unwrap(space.call_function(w_fun, space.wrap(1), space.wrap(2), w_x=space.wrap(1), w_y=space.wrap(2))) == 42

