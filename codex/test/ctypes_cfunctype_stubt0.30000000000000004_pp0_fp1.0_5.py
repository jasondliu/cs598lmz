import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_fun():
    assert fun() == "hello"

def test_fun_call_with_arg():
    raises(TypeError, fun, 1)

def test_fun_call_with_kwargs():
    raises(TypeError, fun, x=1)

def test_fun_call_with_args_and_kwargs():
    raises(TypeError, fun, 1, x=1)

def test_fun_call_with_too_many_args():
    raises(TypeError, fun, 1, 2)

def test_fun_call_with_too_many_args_and_kwargs():
    raises(TypeError, fun, 1, 2, x=1)

def test_fun_call_with_too_few_args():
    raises(TypeError, fun, 1)

def test_fun_call_with_too_few_args_and_kwargs():
    raises(TypeError, fun, x=1)

