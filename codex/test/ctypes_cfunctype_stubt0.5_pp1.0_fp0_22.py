import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_cfunc():
    assert fun() == 1

def test_cfunc_doc():
    assert fun.__doc__ is None

def test_cfunc_name():
    assert fun.__name__ == 'fun'

def test_cfunc_module():
    assert fun.__module__ == '__main__'

def test_cfunc_defaults():
    assert fun.__defaults__ is None

def test_cfunc_dict():
    assert fun.__dict__ == {}

def test_cfunc_closure():
    assert fun.__closure__ is None

def test_cfunc_code():
    assert fun.__code__ is None

def test_cfunc_annotations():
    assert fun.__annotations__ == {}

def test_cfunc_kwdefaults():
    assert fun.__kwdefaults__ is None

def test_cfunc_call():
    assert fun() == 1

