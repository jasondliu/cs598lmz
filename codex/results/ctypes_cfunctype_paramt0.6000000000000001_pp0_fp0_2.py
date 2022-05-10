import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def test_types():
    def f(x, y):
        return x + y
    f_c = FUNTYPE(f)
    assert f_c(1, 2) == 3
    #
    f_c = FUNTYPE(lambda x, y: x + y)
    assert f_c(1, 2) == 3
    #
    f_c = FUNTYPE(lambda x, y: x + y)
    assert f_c(1, 2) == 3

def test_types_2():
    def f(x, y):
        return x + y
    f_c = FUNTYPE(f)
    assert f_c(1, 2) == 3

def test_types_3():
    def f(x, y):
        return x + y
    f_c = FUNTYPE(f)
    assert f_c(1, 2) == 3

def test_types_4():
    def f(x, y):
        return x + y
