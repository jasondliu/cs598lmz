import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def test_fun():
    assert fun() == 42

def test_fun_no_arg():
    try:
        FUNTYPE(lambda: None)
    except TypeError:
        pass
    else:
        raise AssertionError("Did not raise TypeError")

def test_fun_wrong_arg():
    try:
        FUNTYPE(lambda x: None)
    except TypeError:
        pass
    else:
        raise AssertionError("Did not raise TypeError")

def test_fun_wrong_arg_2():
    try:
        FUNTYPE(lambda x, y: None)
    except TypeError:
        pass
    else:
        raise AssertionError("Did not raise TypeError")

def test_fun_wrong_arg_3():
    try:
        FUNTYPE(lambda x, y, z: None)
    except TypeError:
        pass
    else:
        raise AssertionError("Did not raise TypeError")

def test_fun_wrong_res():
    try:
        FUNTYPE(lambda
