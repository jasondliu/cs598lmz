import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 0

def test_fun():
    assert fun() == 0

def test_fun_callable():
    assert callable(fun)

def test_fun_type():
    assert type(fun) is FUNTYPE

def test_fun_repr():
    assert repr(fun) == "<CFUNCTYPE(c_object_p) object at 0x%x>" % (
        id(fun),)

def test_fun_str():
    assert str(fun) == "<CFUNCTYPE(c_object_p) object at 0x%x>" % (
        id(fun),)

def test_fun_doc():
    assert fun.__doc__ is None

def test_fun_name():
    assert fun.__name__ == 'fun'

def test_fun_module():
    assert fun.__module__ == __name__

def test_fun_dict():
    assert fun.__dict__ == {}

def test_fun_closure():
    assert fun.__closure__ is None

