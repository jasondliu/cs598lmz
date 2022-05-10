import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_funtype():
    assert fun() == "hello"

def test_funtype_doc():
    assert fun.__doc__ == None

def test_funtype_name():
    assert fun.__name__ == 'fun'

def test_funtype_module():
    assert fun.__module__ == __name__

def test_funtype_dict():
    assert fun.__dict__ == {}

def test_funtype_weakref():
    import _weakref
    assert isinstance(fun.__weakref__, _weakref.ReferenceType)

def test_funtype_call():
    assert fun() == "hello"

def test_funtype_call_args():
    raises(TypeError, fun, 1)

def test_funtype_call_kwargs():
    raises(TypeError, fun, kw=1)

def test_funtype_call_varargs():
    raises(TypeError, fun, 1, 2, 3)

def test_funtype_repr():
    assert repr
