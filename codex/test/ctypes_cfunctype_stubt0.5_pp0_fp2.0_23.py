import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_fun():
    assert fun()==1

@FUNTYPE
def fun2(x):
    return x

def test_fun2():
    assert fun2(1)==1

def test_fun2_exc():
    py.test.raises(TypeError, "fun2(1, 2)")

def test_fun2_exc2():
    py.test.raises(TypeError, "fun2()")

@FUNTYPE
def fun3(x, y):
    return x+y

def test_fun3():
    assert fun3(1, 2)==3

def test_fun3_exc():
    py.test.raises(TypeError, "fun3(1)")

def test_fun3_exc2():
    py.test.raises(TypeError, "fun3()")

@FUNTYPE
def fun4(x, y, z):
    return x+y+z

def test_fun4():
    assert fun4(1, 2, 3)==6


