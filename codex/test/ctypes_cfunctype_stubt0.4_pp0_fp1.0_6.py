import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def test_function_type():
    assert type(fun) is FUNTYPE
    assert fun() is None

def test_function_type_call():
    assert FUNTYPE(fun)() is None

def test_function_type_call_error():
    raises(TypeError, FUNTYPE, lambda: None)

def test_function_type_call_error2():
    raises(TypeError, FUNTYPE, lambda x: None)

def test_function_type_call_error3():
    raises(TypeError, FUNTYPE, lambda x, y: None)

def test_function_type_call_error4():
    raises(TypeError, FUNTYPE, lambda x, y, z: None)

def test_function_type_call_error5():
    raises(TypeError, FUNTYPE, lambda x, y, z, w: None)

def test_function_type_call_error6():
    raises(TypeError, FUNTYPE, lambda x, y, z, w, v: None)

