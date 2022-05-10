import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

@FUNTYPE
def bar(x):
    return x

@FUNTYPE
def bar_as_list(x):
    return [x]

def test_call():
    assert fun() == 42

def test_call_int():
    assert bar(5) == 5

def test_call_list():
    assert bar_as_list(5) == [5]
