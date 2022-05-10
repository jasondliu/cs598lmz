import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def test_fun():
    assert fun() is None

def test_fun_doc():
    assert fun.__doc__ is None

def test_fun_name():
    assert fun.__name__ == 'fun'

def test_fun_module():
    assert fun.__module__ == __name__

def test_fun_dict():
    assert fun.__dict__ == {}

def test_fun_closure():
    assert fun.__closure__ == (None,)

def test_fun_code():
    assert fun.__code__.co_argcount == 0

def test_fun_defaults():
    assert fun.__defaults__ == None

def test_fun_globals():
    assert fun.__globals__ == globals()

def test_fun_annotations():
    assert fun.__annotations__ == {}

def test_fun_kwdefaults():
    assert fun.__kwdefaults__ == None

def test_fun_call():
    assert fun() is None

