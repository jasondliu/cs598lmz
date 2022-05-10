import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hello'

def test_simple():
    assert fun() == 'hello'

def test_simple_with_call():
    assert call(fun) == 'hello'

def test_simple_with_call_and_args():
    assert call(fun, 1, 2, 3) == 'hello'

def test_simple_with_call_and_kwargs():
    assert call(fun, a=1, b=2, c=3) == 'hello'

def test_simple_with_call_and_args_and_kwargs():
    assert call(fun, 1, 2, 3, a=1, b=2, c=3) == 'hello'

def test_simple_with_call_and_args_and_kwargs_and_varargs():
    assert call(fun, 1, 2, 3, *(4, 5, 6), a=1, b=2, c=3) == 'hello'

def test_simple_with_call_and_args_and_kwargs_and_varargs_and_varkw
