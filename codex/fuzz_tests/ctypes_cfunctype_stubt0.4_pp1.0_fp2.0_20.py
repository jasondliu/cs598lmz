import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_fun():
    assert fun() == 1

def test_fun_in_class():
    class X(object):
        fun = fun
    assert X().fun() == 1

def test_fun_in_class_in_class():
    class X(object):
        class Y(object):
            fun = fun
    assert X.Y.fun() == 1
