import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "fun"

def test_fun():
    assert fun() == "fun"

def test_fun_type():
    assert type(fun) is FUNTYPE

def test_fun_type_repr():
    assert repr(FUNTYPE) == "<type 'CFUNCTYPE'>"

def test_fun_type_str():
    assert str(FUNTYPE) == "<type 'CFUNCTYPE'>"

def test_fun_repr():
    assert repr(fun) == "<CFUNCTYPE object at 0x%x>" % (id(fun),)

def test_fun_str():
    assert str(fun) == "<CFUNCTYPE object at 0x%x>" % (id(fun),)

def test_fun_doc():
    assert fun.__doc__ is None

def test_fun_name():
    assert fun.__name__ == '<lambda>'

def test_fun_module():
    assert fun.__module__ == __name__

def test_fun_dict():
    assert fun.__dict
