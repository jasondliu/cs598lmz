import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def test_fun():
    assert fun() == 42

def test_fun_callable():
    assert callable(fun)

def test_fun_callable_from_python():
    assert callable(fun)
    assert fun() == 42

def test_fun_callable_from_python_and_c():
    assert callable(fun)
    assert fun() == 42
    assert ctypes.pythonapi.PyObject_CallFunction(fun, None) == 42

def test_fun_callable_from_python_and_c_by_name():
    assert callable(fun)
    assert fun() == 42
    assert ctypes.pythonapi.PyObject_CallFunction(fun, None) == 42

def test_fun_callable_from_python_and_c_by_name_and_address():
    assert callable(fun)
    assert fun() == 42
    assert ctypes.pythonapi.PyObject_CallFunction(fun, None) == 42

