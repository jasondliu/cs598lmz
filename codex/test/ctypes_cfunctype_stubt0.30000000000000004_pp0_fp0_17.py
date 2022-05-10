import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def test_fun():
    assert fun() == 42

def test_fun_from_address():
    assert ctypes.CFUNCTYPE(ctypes.py_object)(fun)() == 42

def test_fun_from_address_as_int():
    assert ctypes.CFUNCTYPE(ctypes.py_object)(int(fun))() == 42

def test_fun_from_address_as_long():
    assert ctypes.CFUNCTYPE(ctypes.py_object)(long(fun))() == 42

def test_fun_from_address_as_float():
    assert ctypes.CFUNCTYPE(ctypes.py_object)(float(fun))() == 42

def test_fun_from_address_as_string():
    assert ctypes.CFUNCTYPE(ctypes.py_object)(str(fun))() == 42

