import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_fun():
    assert fun() == "hello"

def test_fun_call():
    assert fun()() == "hello"

def test_fun_call_args():
    assert fun()("hello", "world") == "hello"

def test_fun_call_kwargs():
    assert fun()(hello="world") == "hello"

def test_fun_call_args_kwargs():
    assert fun()("hello", world="world") == "hello"

def test_fun_call_args_kwargs_call():
    assert fun()("hello", world="world")() == "hello"

def test_fun_call_args_kwargs_call_args():
    assert fun()("hello", world="world")("hello", "world") == "hello"

def test_fun_call_args_kwargs_call_kwargs():
    assert fun()("hello", world="world")(hello="world") == "hello"

