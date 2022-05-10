import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def test_function_type_args():
    assert fun.__name__ == 'fun'
    raises(TypeError, fun, 42)
    raises(TypeError, fun, 42, 42)

def test_function_type_result():
    raises(TypeError, type(fun), type)
    assert type(fun) is FUNTYPE
    assert FUNTYPE(fun) is fun

def test_function_type_call():
    assert fun() is None

def test_function_type_repr():
    assert repr(fun) == "<built-in function fun>"

def test_function_type_doc():
    assert fun.__doc__ is None

def test_function_type_dict():
    assert fun.__dict__ == {'__name__': 'fun'}
    raises(TypeError, "fun.__dict__ = 42")

def test_function_type_get():
    assert fun.__module__ == __name__
    raises(TypeError, "fun.__module__ = 42")

