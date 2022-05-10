import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_function():
    assert fun() == "hello"

@FUNTYPE
def fun2(x):
    return x

def test_function2():
    assert fun2(42) == 42

@FUNTYPE
def fun3(x, y, z):
    return x + y + z

def test_function3():
    assert fun3(1, 2, 3) == 6

@FUNTYPE
def fun4(x, y, z, t):
    return x + y + z + t

def test_function4():
    assert fun4(1, 2, 3, 4) == 10

@FUNTYPE
def fun5(x, y, z, t, u):
    return x + y + z + t + u

def test_function5():
    assert fun5(1, 2, 3, 4, 5) == 15

@FUNTYPE
def fun6(x, y, z, t, u, v):
    return x + y + z + t + u + v

