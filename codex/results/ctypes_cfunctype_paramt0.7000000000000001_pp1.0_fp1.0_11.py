import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def check_pow(x, y):
    return x**y

check_pow_ = FUNTYPE(check_pow)
# check_pow_ = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(check_pow)

def test_pow(x, y):
    return x**y

test_pow_ = FUNTYPE(test_pow)
# test_pow_ = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(test_pow)

compare_functions(check_pow_, test_pow_, 'pow')

def check_add(x, y):
    return x + y

check_add_ = FUNTYPE(check_add)
# check_add_ = ctypes.CFUNCTYPE(ctypes.c_int, ctypes
