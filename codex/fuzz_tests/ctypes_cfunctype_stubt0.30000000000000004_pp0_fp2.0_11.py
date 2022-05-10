import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_call_function(space):
    w_res = space.call_function(space.wrap(fun))
    assert space.str_w(w_res) == "hello"

def test_call_method(space):
    w_res = space.call_method(space.wrap("hello"), "upper")
    assert space.str_w(w_res) == "HELLO"

def test_call_method_varargs(space):
    w_res = space.call_method(space.wrap("hello"), "replace", space.wrap("l"), space.wrap("w"), space.wrap(1))
    assert space.str_w(w_res) == "hewlo"

def test_call_function_varargs(space):
    w_res = space.call_function(space.wrap(int), space.wrap("42"), space.wrap(16))
    assert space.int_w(w_res) == 66

def test_call_function_kwargs(space):
    w_res = space.call
