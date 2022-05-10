import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_c_int_sizeof():
    assert ctypes.c_int.sizeof() == 4

def test_c_int_add():
    assert ctypes.c_int.__add__(1, 2) == 3

def test_c_int_sub():
    assert ctypes.c_int.__sub__(1, 2) == -1

def test_c_int_mul():
    assert ctypes.c_int.__mul__(3, 4) == 12

def test_c_int_div():
    assert ctypes.c_int.__div__(6, 3) == 2

def test_c_int_mod():
    assert ctypes.c_int.__mod__(6, 3) == 0

def test_c_int_invert():
    assert ctypes.c_int.__invert__(3) == -4

def test_c_int_lshift():
    assert ctypes.c_int.__lshift__(1, 2) == 4

def test_
