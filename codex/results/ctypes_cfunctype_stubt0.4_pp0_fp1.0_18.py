import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_fun():
    assert fun() == 1

def test_fun_type():
    assert type(fun) is FUNTYPE

def test_fun_type_call():
    assert type(fun()) is int

def test_fun_type_call_call():
    assert type(fun()()) is int

def test_fun_type_call_call_call():
    assert type(fun()()()) is int

def test_fun_type_call_call_call_call():
    assert type(fun()()()()) is int

def test_fun_type_call_call_call_call_call():
    assert type(fun()()()()()) is int

def test_fun_type_call_call_call_call_call_call():
    assert type(fun()()()()()()) is int

def test_fun_type_call_call_call_call_call_call_call():
    assert type(fun()()()()()()()) is int

def test_fun_type_call_call_call_call
