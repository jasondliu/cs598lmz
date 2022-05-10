import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

@FUNTYPE
def fun2():
    return 2

def test_fun():
    assert fun() == 1
    assert fun2() == 2

def test_fun_2():
    assert fun() == 1
    assert fun2() == 2

def test_fun_3():
    assert fun() == 1
    assert fun2() == 2

def test_fun_4():
    assert fun() == 1
    assert fun2() == 2

def test_fun_5():
    assert fun() == 1
    assert fun2() == 2

def test_fun_6():
    assert fun() == 1
    assert fun2() == 2

def test_fun_7():
    assert fun() == 1
    assert fun2() == 2

def test_fun_8():
    assert fun() == 1
    assert fun2() == 2

def test_fun_9():
    assert fun() == 1
    assert fun2() == 2

def test_fun_10():
    assert fun() == 1
    assert fun2() == 2
