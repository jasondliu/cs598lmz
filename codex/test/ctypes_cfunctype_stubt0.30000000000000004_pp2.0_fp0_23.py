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
    assert fun2(42) == 42

@FUNTYPE
def fun3(x, y):
    return x + y

def test_fun3():
    assert fun3(41, 1) == 42

@FUNTYPE
def fun4(x, y, z):
    return x + y + z

def test_fun4():
    assert fun4(40, 1, 1) == 42

@FUNTYPE
def fun5(x, y, z, t):
    return x + y + z + t

def test_fun5():
    assert fun5(40, 1, 1, 0) == 42

@FUNTYPE
def fun6(x, y, z, t, u):
    return x + y + z + t + u

def test_fun6():
    assert fun6(40, 1, 1, 0, 0) == 42

