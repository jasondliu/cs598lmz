import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello, World"

def test_call_c_function():
    assert "Hello, World" == fun()

def test_call_c_function_from_python():
    f = fun
    assert "Hello, World" == f()

def test_call_c_function_from_python_twice():
    f = fun
    assert "Hello, World" == f()
    assert "Hello, World" == f()

def test_call_c_function_from_python_twice_from_different_functions():
    f = fun
    assert "Hello, World" == f()
    assert "Hello, World" == fun()

