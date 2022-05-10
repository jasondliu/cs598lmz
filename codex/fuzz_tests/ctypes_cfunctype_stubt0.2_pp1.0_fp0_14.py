import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_fun():
    assert fun() == "hello"

def test_fun_type():
    assert type(fun) == FUNTYPE

def test_fun_type_name():
    assert fun.__name__ == "fun"

def test_fun_type_doc():
    assert fun.__doc__ == None

def test_fun_type_module():
    assert fun.__module__ == "test_fun"

def test_fun_type_dict():
    assert fun.__dict__ == {}

def test_fun_type_closure():
    assert fun.__closure__ == None

def test_fun_type_code():
    assert fun.__code__ == None

def test_fun_type_defaults():
    assert fun.__defaults__ == None

def test_fun_type_globals():
    assert fun.__globals__ == globals()

def test_fun_type_annotations():
    assert fun.__annotations__ == {}

def test_fun_type_kw
