import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def test_fun():
    assert fun() == 42

def test_fun_type():
    assert type(fun) is FUNTYPE

def test_fun_type_repr():
    assert repr(FUNTYPE) == "<class 'ctypes.CFUNCTYPE'>"

def test_fun_repr():
    assert repr(fun) == "<CFunctionType object at 0x%x>" % (id(fun),)

def test_fun_doc():
    assert fun.__doc__ == None

def test_fun_name():
    assert fun.__name__ == 'fun'

def test_fun_module():
    assert fun.__module__ == __name__

def test_fun_dict():
    assert fun.__dict__ == {}

def test_fun_call():
    assert fun() == 42

def test_fun_call_args():
    raises(TypeError, fun, 1)

def test_fun_call_kwargs():
    raises(TypeError, fun, x=1)

def test_fun
