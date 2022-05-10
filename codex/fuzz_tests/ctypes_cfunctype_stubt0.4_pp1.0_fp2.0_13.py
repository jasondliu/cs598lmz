import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def fun2():
    return fun()

def test_fun2():
    assert fun2() == "hello"

def fun3():
    return fun2()

def test_fun3():
    assert fun3() == "hello"

def fun4():
    return fun3()

def test_fun4():
    assert fun4() == "hello"

def fun5():
    return fun4()

def test_fun5():
    assert fun5() == "hello"

def fun6():
    return fun5()

def test_fun6():
    assert fun6() == "hello"

def fun7():
    return fun6()

def test_fun7():
    assert fun7() == "hello"

def fun8():
    return fun7()

def test_fun8():
    assert fun8() == "hello"

def fun9():
    return fun8()

def test_fun9():
    assert fun9() == "hello"

def fun10():
    return fun9
