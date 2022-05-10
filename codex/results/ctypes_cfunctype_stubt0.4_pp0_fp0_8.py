import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello World"

def test_fun():
    assert fun() == "Hello World"

def test_fun_type():
    assert type(fun) is FUNTYPE

def test_fun_callable():
    assert callable(fun)

def test_fun_call():
    assert fun() == "Hello World"

def test_fun_call_type():
    assert type(fun()) == str

def test_fun_call_type_int():
    assert type(int(fun())) == int

def test_fun_call_type_str():
    assert type(str(fun())) == str

def test_fun_call_type_float():
    assert type(float(fun())) == float

def test_fun_call_type_bool():
    assert type(bool(fun())) == bool

def test_fun_call_type_list():
    assert type(list(fun())) == list

def test_fun_call_type_tuple():
    assert type(tuple(fun())) == tuple

def test
