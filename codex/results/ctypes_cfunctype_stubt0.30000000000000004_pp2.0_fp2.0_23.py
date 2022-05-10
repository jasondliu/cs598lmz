import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_fun():
    assert fun() == "hello"

def test_fun_type():
    assert type(fun) is FUNTYPE

def test_fun_callable():
    assert callable(fun)

def test_fun_call():
    assert fun() == "hello"

def test_fun_call_type():
    assert type(fun()) is str

def test_fun_call_type_2():
    assert type(fun()()) is str

def test_fun_call_type_3():
    assert type(fun()()()) is str

def test_fun_call_type_4():
    assert type(fun()()()()) is str

def test_fun_call_type_5():
    assert type(fun()()()()()) is str

def test_fun_call_type_6():
    assert type(fun()()()()()()) is str

def test_fun_call_type_7():
    assert type(fun()()()()()()()) is str

def test_fun
