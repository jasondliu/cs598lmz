import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_fun():
    assert fun() == 1

def test_fun_call():
    assert fun() == 1

def test_fun_call_again():
    assert fun() == 1

def test_fun_call_again_again():
    assert fun() == 1

def test_fun_call_again_again_again():
    assert fun() == 1

def test_fun_call_again_again_again_again():
    assert fun() == 1

def test_fun_call_again_again_again_again_again():
    assert fun() == 1

def test_fun_call_again_again_again_again_again_again():
    assert fun() == 1

def test_fun_call_again_again_again_again_again_again_again():
    assert fun() == 1

def test_fun_call_again_again_again_again_again_again_again_again():
    assert fun() == 1

