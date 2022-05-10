import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'fun'

def test_cfunc_callable():
    assert callable(fun)

def test_cfunc_repr():
    assert repr(fun) == '<CFunctionType object at 0x%x>' % (id(fun),)

def test_cfunc_doc():
    assert fun.__doc__ is None

def test_cfunc_name():
    assert fun.__name__ == 'fun'

def test_cfunc_module():
    assert fun.__module__ == '__main__'

def test_cfunc_defaults():
    assert fun.__defaults__ == ()

def test_cfunc_globals():
    assert fun.__globals__ == globals()

def test_cfunc_dict():
    assert fun.__dict__ == {}

def test_cfunc_closure():
    assert fun.__closure__ == None

def test_cfunc_annotations():
    assert fun.__annotations__ == {}

def test_cfunc_kwdefaults():
    assert fun
