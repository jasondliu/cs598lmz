import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_fun():
    assert fun() == 1

def test_fun_type():
    assert type(fun) is FUNTYPE

def test_fun_type_fun():
    assert type(fun)() == 1

def test_fun_type_fun_type():
    assert type(type(fun)) is type

def test_fun_type_fun_type_fun():
    assert type(type(fun))() == 1

def test_fun_type_fun_type_fun_type():
    assert type(type(type(fun))) is type

def test_fun_type_fun_type_fun_type_fun():
    assert type(type(type(fun)))() == 1

def test_fun_type_fun_type_fun_type_fun_type():
    assert type(type(type(type(fun)))) is type

def test_fun_type_fun_type_fun_type_fun_type_fun():
    assert type(type(type(type(fun))))() == 1

