import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_function():
    assert fun() == "hello"

def test_function_call():
    assert fun()() == "hello"

def test_function_call_call():
    assert fun()()() == "hello"

def test_function_call_call_call():
    assert fun()()()() == "hello"

def test_function_call_call_call_call():
    assert fun()()()()() == "hello"

def test_function_call_call_call_call_call():
    assert fun()()()()()() == "hello"

def test_function_call_call_call_call_call_call():
    assert fun()()()()()()() == "hello"

def test_function_call_call_call_call_call_call_call():
    assert fun()()()()()()()() == "hello"

