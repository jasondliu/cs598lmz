import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_fun():
    assert fun() == "hello"

@FUNTYPE
def fun2(x):
    return x

def test_fun2():
    assert fun2(5) == 5

@FUNTYPE
def fun3(x, y):
    return x + y

def test_fun3():
    assert fun3(5, 6) == 11

@FUNTYPE
def fun4(x, y, z):
    return x + y + z

def test_fun4():
    assert fun4(5, 6, 7) == 18

@FUNTYPE
def fun5(x, y, z, w):
    return x + y + z + w

def test_fun5():
    assert fun5(5, 6, 7, 8) == 26

@FUNTYPE
def fun6(x, y, z, w, v):
    return x + y + z + w + v

def test_fun6():
    assert fun6(5, 6, 7, 8, 9) == 35

@FUN
