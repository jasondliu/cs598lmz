import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def test_cfuntype():
    assert fun() == 42

def test_cfuntype_callable():
    assert callable(fun)

def test_cfuntype_repr():
    assert repr(fun) == '<CFunctionType object at 0x%x>' % (id(fun),)

def test_cfuntype_doc():
    assert fun.__doc__ is None

def test_cfuntype_name():
    assert fun.__name__ == 'fun'

def test_cfuntype_module():
    assert fun.__module__ == __name__

def test_cfuntype_dict():
    assert fun.__dict__ == {}

def test_cfuntype_closure():
    assert fun.__closure__ is None

def test_cfuntype_code():
    assert fun.__code__ is None

def test_cfuntype_defaults():
    assert fun.__defaults__ is None

def test_cfuntype_globals():
    assert fun.__globals__
