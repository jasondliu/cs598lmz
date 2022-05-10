import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_fun():
    assert fun() == "hello"

def test_fun_p():
    assert fun.__closure__[0].cell_contents == "hello"

def test_fun_p_wrapper():
    assert fun.__closure__[0].__closure__[0].cell_contents == "hello"

def test_fun_p_wrapper_wrapper():
    assert fun.__closure__[0].__closure__[0].__closure__[0].cell_contents == "hello"

def test_fun_p_wrapper_wrapper_wrapper():
    assert fun.__closure__[0].__closure__[0].__closure__[0].__closure__[0].cell_contents == "hello"

def test_fun_p_wrapper_wrapper_wrapper_wrapper():
    assert fun.__closure__[0].__closure__[0].__closure__[0].__closure__[0].__closure__[0].cell_contents == "hello"

def test_fun_p_wrapper_wrapper_wrapper
