import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_func(x):
    return x

FUNTYPE2 = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)

@FUNTYPE2
def fun2(x):
    return x

def test_func2(x):
    return x

def test_func3(x, y):
    return x

def test_func4(x, y):
    return x

def test_func5(x, y):
    return x

def test_func6(x, y):
    return x

def test_func7(x, y):
    return x

def test_func8(x, y):
    return x

def test_func9(x, y):
    return x

def test_func10(x, y):
    return x

def test_func11(x, y):
    return x

def test_func12(x, y):
    return x

def test_func13(x, y):
    return x

