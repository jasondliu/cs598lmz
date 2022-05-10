import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_fun():
    assert fun() == "hello"

def test_fun_type():
    assert type(fun) is FUNTYPE

def test_fun_type_type():
    assert type(type(fun)) is type

def test_fun_type_type_type():
    assert type(type(type(fun))) is type

def test_fun_type_type_type_type():
    assert type(type(type(type(fun)))) is type
