import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_function():
    assert fun() == "hello"

def test_function_type():
    assert type(fun) is FUNTYPE

def test_function_type_is_callable():
    assert callable(FUNTYPE)

def test_function_type_is_not_callable():
    assert not callable(ctypes.c_int)

def test_function_type_is_not_callable2():
    assert not callable(ctypes.c_int())

def test_function_type_is_not_callable3():
    assert not callable(ctypes.c_int(42))

def test_function_type_is_not_callable4():
    assert not callable(ctypes.c_int.in_dll(ctypes.pythonapi, "Py_True"))

def test_function_type_is_not_callable5():
    assert not callable(ctypes.c_int.in_dll(ctypes.pythonapi, "Py_False"))
