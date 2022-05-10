import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_ctypes():
    assert fun() == 1

def test_ctypes_call_with_wrong_arguments():
    raises(TypeError, fun, 1)

def test_ctypes_call_with_too_many_arguments():
    raises(TypeError, fun, 1, 2)

def test_ctypes_call_with_too_few_arguments():
    raises(TypeError, fun)

def test_ctypes_call_with_wrong_result():
    raises(TypeError, ctypes.cast, fun, ctypes.c_int)

def test_ctypes_call_with_wrong_result_type():
    raises(TypeError, ctypes.cast, fun, ctypes.c_void_p)

def test_ctypes_call_with_wrong_result_type2():
    raises(TypeError, ctypes.cast, fun, ctypes.c_char_p)

