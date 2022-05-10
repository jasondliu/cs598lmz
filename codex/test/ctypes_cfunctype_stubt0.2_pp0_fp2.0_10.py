import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_fun():
    assert fun() == "hello"

def test_fun_type():
    assert type(fun) == FUNTYPE

def test_fun_type_call():
    assert fun() == "hello"

def test_fun_type_call_type():
    assert type(fun()) == str

def test_fun_type_call_type_type():
    assert type(type(fun())) == type

def test_fun_type_call_type_type_type():
    assert type(type(type(fun()))) == type

def test_fun_type_call_type_type_type_type():
    assert type(type(type(type(fun())))) == type

def test_fun_type_call_type_type_type_type_type():
    assert type(type(type(type(type(fun()))))) == type

