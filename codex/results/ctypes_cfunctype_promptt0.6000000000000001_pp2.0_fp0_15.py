import ctypes
# Test ctypes.CFUNCTYPE()

@CFUNCTYPE(c_int)
def func_int_0(a):
    return a

@CFUNCTYPE(c_int, c_int)
def func_int_1(a):
    return a

@CFUNCTYPE(c_int, c_int, c_int)
def func_int_2(a, b):
    return a + b

@CFUNCTYPE(c_int, c_int, c_int, c_int)
def func_int_3(a, b, c):
    return a + b + c

@CFUNCTYPE(c_int, c_int, c_int, c_int, c_int)
def func_int_4(a, b, c, d):
    return a + b + c + d

@CFUNCTYPE(c_int, c_int, c_int, c_int, c_int, c_int)
def func_int_5(a, b, c, d, e):
    return a
