import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def make_wrapper(func):
    return FUNTYPE(func)

def test_wrapper(func):
    f = make_wrapper(func)
    for i in range(100):
        f(i)

def test_func(x):
    return x ** 2

def test_func2(x):
    return x ** 3

def test_func3(x):
    return x ** 4

def test_func4(x):
    return x ** 5

def test_func5(x):
    return x ** 6

def test_func6(x):
    return x ** 7

def test_func7(x):
    return x ** 8

def test_func8(x):
    return x ** 9

def test_func9(x):
    return x ** 10

def test_func10(x):
    return x ** 11

def test_func11(x):
    return x ** 12

def test_func12(x):
    return x **
