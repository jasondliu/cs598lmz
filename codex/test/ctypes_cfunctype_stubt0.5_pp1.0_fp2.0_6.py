import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def fun_as_obj(space):
    return space.wrap(fun)

def test_call_c_function(space):
    w_f = space.appexec([], fun_as_obj)
    assert space.int_w(space.call_function(w_f)) == 42

def test_call_c_function_with_args(space):
    w_f = space.appexec([], fun_as_obj)
    assert space.int_w(space.call_function(w_f, space.wrap(1), space.wrap(2))) == 42

def test_call_c_function_with_kwargs(space):
    w_f = space.appexec([], fun_as_obj)
    assert space.int_w(space.call_function(w_f, w_a=space.wrap(1), w_b=space.wrap(2))) == 42

