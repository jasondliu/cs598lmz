import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 5

def test_fun():
    assert fun() == 5

def test_fun_type():
    assert type(fun) is FUNTYPE

def test_fun_type_call():
    assert fun() == 5

def test_fun_type_call_type():
    assert type(fun()) is int

def test_fun_type_call_type_instance():
    assert isinstance(fun(), int)

def test_fun_type_call_type_instance_base():
    assert issubclass(int, object)

def test_fun_type_call_type_instance_base_fail():
    assert not issubclass(object, int)

def test_fun_type_call_type_instance_base_fail_msg():
    try:
        assert not issubclass(object, int)
    except AssertionError as e:
        assert str(e) == "issubclass(object, int) is not True"

