import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

def f(x):
    return x

def g(x):
    return x

def h(x):
    return x

def test(x):
    return f(g(h(x)))

def test_large(x):
    return f(g(h(x)))

def test_large2(x):
    return f(g(h(x)))

def test_large3(x):
    return f(g(h(x)))

def test_large4(x):
    return f(g(h(x)))

def test_large5(x):
    return f(g(h(x)))

def test_large6(x):
    return f(g(h(x)))

def test_large7(x):
    return f(g(h(x)))

def test_large8(x):
    return f(g(h(x)))

def test_large9(x
