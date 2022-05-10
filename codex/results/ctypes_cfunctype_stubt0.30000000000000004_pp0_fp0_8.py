import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_fun():
    assert fun() == "hello"

def test_fun2():
    assert fun() == "hello"

def test_fun3():
    assert fun() == "hello"

def test_fun4():
    assert fun() == "hello"

def test_fun5():
    assert fun() == "hello"

def test_fun6():
    assert fun() == "hello"

def test_fun7():
    assert fun() == "hello"

def test_fun8():
    assert fun() == "hello"

def test_fun9():
    assert fun() == "hello"

def test_fun10():
    assert fun() == "hello"

def test_fun11():
    assert fun() == "hello"

def test_fun12():
    assert fun() == "hello"

def test_fun13():
    assert fun() == "hello"

def test_fun14():
    assert fun() == "hello"

def test_fun15():
    assert fun()
