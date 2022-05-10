import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

def f(x):
    return x.x + x.y

def test_add(x):
    x.x = 1
    f(x)

def test_add_no_side_effect(x):
    f(x)

def test_add2():
    x = C()
    f(x)

def test_add3(x):
    f(x)

def test_add_no_side_effect_constant(x):
    f(C())

def test_add_no_side_effect_constant_constant():
    f(C())

def test_add_no_side_effect_constant_constant2():
    f(C())

def test_add_no_side_effect_constant_constant3():
    f(C())

def test_add_no_side_effect_constant_constant
