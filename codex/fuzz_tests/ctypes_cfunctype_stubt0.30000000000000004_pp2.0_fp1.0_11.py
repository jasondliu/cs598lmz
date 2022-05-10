import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_c_function():
    assert fun() == "hello"

def test_c_function_callable():
    assert callable(fun)

def test_c_function_call():
    assert fun() == "hello"

def test_c_function_call_args():
    assert fun(1, 2, 3) == "hello"

def test_c_function_call_kwargs():
    assert fun(foo=1, bar=2) == "hello"

def test_c_function_call_args_kwargs():
    assert fun(1, 2, 3, foo=1, bar=2) == "hello"

def test_c_function_repr():
    assert repr(fun) == "<CFunctionType object at 0x%x>" % (id(fun),)

def test_c_function_str():
    assert str(fun) == "<CFunctionType object at 0x%x>" % (id(fun),)

def test_c_function_getattr():
    raises(AttributeError,
