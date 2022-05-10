import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_call_fun():
    assert fun() == 1

def test_call_fun2():
    assert fun() == 1

def test_call_fun3():
    assert fun() == 1

def test_call_fun4():
    assert fun() == 1
