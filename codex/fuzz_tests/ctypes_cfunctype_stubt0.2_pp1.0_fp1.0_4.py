import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def test_fun():
    assert fun() == 42

def test_fun_type():
    assert type(fun) is FUNTYPE

def test_fun_type_call():
    assert fun() == 42

def test_fun_type_call_type():
    assert type(fun()) is int

def test_fun_type_call_type_value():
    assert fun() == 42

def test_fun_type_call_type_value_attr():
    assert fun().real == 42

def test_fun_type_call_type_value_attr_item():
    assert fun().real == 42

def test_fun_type_call_type_value_attr_item_call():
    assert fun().real == 42

def test_fun_type_call_type_value_attr_item_call_type():
    assert type(fun().real) is int

def test_fun_type_call_type_value_attr_item_call_type_value():
    assert fun().real == 42

def test_fun_type_
