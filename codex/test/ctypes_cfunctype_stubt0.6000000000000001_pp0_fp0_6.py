import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_fun1():
    assert fun() == "hello"

@FUNTYPE
def fun2():
    return "hello2"

def test_fun2():
    assert fun2() == "hello2"

@FUNTYPE
def fun3():
    return "hello3"

def test_fun3():
    assert fun3() == "hello3"
