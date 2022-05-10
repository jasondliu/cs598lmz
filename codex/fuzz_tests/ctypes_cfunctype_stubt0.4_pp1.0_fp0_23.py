import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def test_fun():
    assert fun() == 42

def test_fun_callable():
    assert callable(fun)

def test_fun_callable_getattr():
    assert callable(getattr(fun, 'foo'))

def test_fun_callable_getattr_call():
    assert getattr(fun, 'foo')() == 42

def test_fun_callable_getattr_call_callable():
    assert callable(getattr(fun, 'foo')())

def test_fun_callable_getattr_call_callable_call():
    assert getattr(fun, 'foo')()() == 42

def test_fun_callable_getattr_call_callable_call_callable():
    assert callable(getattr(fun, 'foo')()())

def test_fun_callable_getattr_call_callable_call_callable_call():
    assert getattr(fun, 'foo')()()() == 42

def test_fun_callable_getattr_call_
