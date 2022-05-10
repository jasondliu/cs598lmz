import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello"

def test_fun():
    assert fun() == "Hello"

def test_fun_is_callable():
    assert callable(fun)

def test_fun_is_not_a_function():
    assert not isinstance(fun, types.FunctionType)

def test_fun_is_a_function():
    assert isinstance(fun, FUNTYPE)

def test_fun_is_a_callable():
    assert isinstance(fun, collections.Callable)

def test_fun_is_a_callable_with_call():
    assert isinstance(fun, collections.abc.Callable)

def test_fun_is_a_callable_with_call_with_callable():
    assert isinstance(fun, collections.abc.Callable)

def test_fun_is_a_callable_with_call_with_callable_with_call():
    assert isinstance(fun, collections.abc.Callable)

def test_fun_is_a_callable_with_call_with_call
