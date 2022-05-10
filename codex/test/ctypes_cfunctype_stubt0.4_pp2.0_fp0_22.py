import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def test_fun():
    assert fun() == 42

def test_fun_return_type():
    assert type(fun()) is int

def test_fun_return_type_from_c():
    assert type(fun()) is int

def test_fun_return_type_from_c_in_c():
    assert type(fun()) is int

def test_fun_return_type_from_c_in_c_in_c():
    assert type(fun()) is int

def test_fun_return_type_from_c_in_c_in_c_in_c():
    assert type(fun()) is int

def test_fun_return_type_from_c_in_c_in_c_in_c_in_c():
    assert type(fun()) is int

def test_fun_return_type_from_c_in_c_in_c_in_c_in_c_in_c():
    assert type(fun()) is int

