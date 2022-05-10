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
    assert fun2(1) == 1

@FUNTYPE
def fun3(x, y):
    return x + y

def test_fun3():
    assert fun3(1, 2) == 3

@FUNTYPE
def fun4(x, y, z):
    return x + y + z

def test_fun4():
    assert fun4(1, 2, 3) == 6

@FUNTYPE
def fun5(x, y, z, t):
    return x + y + z + t

def test_fun5():
    assert fun5(1, 2, 3, 4) == 10

@FUNTYPE
def fun6(x, y, z, t, u):
    return x + y + z + t + u

def test_fun6():
    assert fun6(1, 2, 3, 4, 5) == 15

@FUN
