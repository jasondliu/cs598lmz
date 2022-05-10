import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_call_function_with_py_object_return_value():
    assert fun() == "hello"

def test_call_function_with_py_object_return_value_as_int():
    assert int(fun()) == ord("h")

def test_call_function_with_py_object_return_value_as_float():
    assert float(fun()) == ord("h")

def test_call_function_with_py_object_return_value_as_str():
    assert str(fun()) == "hello"

def test_call_function_with_py_object_return_value_as_bool():
    assert bool(fun()) is True

def test_call_function_with_py_object_return_value_as_list():
    assert list(fun()) == ["h", "e", "l", "l", "o"]

