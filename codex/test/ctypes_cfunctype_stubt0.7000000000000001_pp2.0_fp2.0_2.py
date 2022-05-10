import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'a'

def test_fun():
    assert fun() == 'a'

#
# Test that we can do math with floats
#
def test_float():
    a = 12.0
    b = 8.0
    assert a*a == 144.0
    assert b*b == 64.0
    assert (a*a * b*b) == 9216.0
    assert (a*a / b*b) == 2.25
    assert (a*a * b*b) == (a*a * b*b)

#
# Test that we can pass a float as a parameter
#
def test_float_param(x):
    assert x == 3.14

def test_float_call():
    test_float_param(3.14)
    
#
# Test that we can do math with ints
#
def test_int():
    a = 12
    b = 8
    assert a*a == 144
    assert b*b == 64
    assert (a*a * b*b) == 9216
