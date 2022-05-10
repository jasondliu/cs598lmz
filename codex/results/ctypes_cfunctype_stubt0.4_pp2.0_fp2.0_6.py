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

def test_fun_type_str():
    assert str(FUNTYPE) == "<class 'ctypes.CFUNCTYPE'>"

def test_fun_repr():
    assert repr(fun) == "<ctypes.CFUNCTYPE object at 0x%x>" % (id(fun),)

def test_fun_str():
    assert str(fun) == "<ctypes.CFUNCTYPE object at 0x%x>" % (id(fun),)

def test_fun_type_call():
    assert FUNTYPE(fun)() == 42

def test_fun_type_call_type():
    assert type(FUNTYPE(fun)) is FUNTYPE

def test_fun_type_call_repr():
    assert repr(FUNTYPE(fun
