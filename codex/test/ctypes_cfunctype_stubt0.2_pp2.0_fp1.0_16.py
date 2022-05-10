import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def test_fun():
    assert fun() == 42

def test_fun_type():
    assert type(fun) is FUNTYPE

def test_fun_type_type():
    assert type(type(fun)) is type

def test_fun_type_type_type():
    assert type(type(type(fun))) is type

def test_fun_type_type_type_type():
    assert type(type(type(type(fun)))) is type

def test_fun_type_type_type_type_type():
    assert type(type(type(type(type(fun))))) is type

def test_fun_type_type_type_type_type_type():
    assert type(type(type(type(type(type(fun)))))) is type

def test_fun_type_type_type_type_type_type_type():
    assert type(type(type(type(type(type(type(fun))))))) is type

