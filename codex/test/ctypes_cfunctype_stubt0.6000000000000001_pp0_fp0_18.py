import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello World"

def test_py_fun_call():
    assert fun() == "Hello World"

def test_py_fun_type():
    assert type(fun) is FUNTYPE

def test_py_fun_addr():
    assert fun.__code__.co_code == b'\x04\x00\x00\x00\x00\x00\x00\x00'

def test_py_fun_call_2():
    assert fun() == "Hello World"

def test_py_fun_type_2():
    assert type(fun) is FUNTYPE

def test_py_fun_addr_2():
    assert fun.__code__.co_code == b'\x04\x00\x00\x00\x00\x00\x00\x00'
