import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_fun():
    assert fun() == 1

def test_fun_type():
    assert type(fun) is FUNTYPE

def test_fun_type_type():
    assert type(FUNTYPE) is type

def test_fun_type_instance():
    assert isinstance(fun, FUNTYPE)

def test_fun_type_instance_type():
    assert isinstance(FUNTYPE, type)

def test_fun_type_instance_type_type():
    assert isinstance(type, type)

def test_fun_type_instance_type_type_type():
    assert isinstance(type(type), type)

def test_fun_type_instance_type_type_type_type():
    assert isinstance(type(type(type)), type)

def test_fun_type_instance_type_type_type_type_type():
    assert isinstance(type(type(type(type))), type)

def test_fun_type_instance_type_type_type_type_type_type():
    assert is
