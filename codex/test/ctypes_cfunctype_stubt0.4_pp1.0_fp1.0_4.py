import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_py_object_return():
    assert fun() == "hello"

def test_py_object_return_None():
    @FUNTYPE
    def fun():
        return None
    assert fun() is None

def test_py_object_return_int():
    @FUNTYPE
    def fun():
        return 42
    assert fun() == 42

def test_py_object_return_float():
    @FUNTYPE
    def fun():
        return 3.14
    assert fun() == 3.14

def test_py_object_return_str():
    @FUNTYPE
    def fun():
        return "hello"
    assert fun() == "hello"

def test_py_object_return_tuple():
    @FUNTYPE
    def fun():
        return (1, 2, 3)
    assert fun() == (1, 2, 3)

def test_py_object_return_list():
    @FUNTYPE
    def fun():
        return [1, 2, 3]
