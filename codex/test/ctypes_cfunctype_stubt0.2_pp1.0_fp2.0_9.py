import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_fun():
    assert fun() == "hello"

def test_fun_call():
    assert fun.__call__() == "hello"

def test_fun_call_call():
    assert fun.__call__.__call__() == "hello"

def test_fun_call_call_call():
    assert fun.__call__.__call__.__call__() == "hello"

def test_fun_call_call_call_call():
    assert fun.__call__.__call__.__call__.__call__() == "hello"

def test_fun_call_call_call_call_call():
    assert fun.__call__.__call__.__call__.__call__.__call__() == "hello"

def test_fun_call_call_call_call_call_call():
    assert fun.__call__.__call__.__call__.__call__.__call__.__call__() == "hello"

