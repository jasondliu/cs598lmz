import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 0

def test_fun():
    assert fun() == 0

def test_fun_with_error():
    raises(TypeError, FUNTYPE, lambda: None)

def test_fun_with_error2():
    raises(TypeError, FUNTYPE, lambda x: None)

def test_fun_with_error3():
    raises(TypeError, FUNTYPE, lambda x, y: None)

def test_fun_with_error4():
    raises(TypeError, FUNTYPE, lambda x, y, z: None)

def test_fun_with_error5():
    raises(TypeError, FUNTYPE, lambda x, y, z, t: None)

def test_fun_with_error6():
    raises(TypeError, FUNTYPE, lambda x, y, z, t, u: None)

def test_fun_with_error7():
    raises(TypeError, FUNTYPE, lambda x, y, z, t, u, v: None)

def test_fun_with_error8():
    raises(TypeError, FUNTYPE
