import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_py_object_returns():
    assert fun() == 1

def test_py_object_returns_null():
    @FUNTYPE
    def fun():
        return None
    assert fun() is None

def test_py_object_returns_int():
    @FUNTYPE
    def fun():
        return 1
    assert fun() == 1

def test_py_object_returns_float():
    @FUNTYPE
    def fun():
        return 1.5
    assert fun() == 1.5

def test_py_object_returns_complex():
    @FUNTYPE
    def fun():
        return 1.5 + 0.5j
    assert fun() == 1.5 + 0.5j

def test_py_object_returns_string():
    @FUNTYPE
    def fun():
        return 'xxx'
    assert fun() == 'xxx'

def test_py_object_returns_unicode():
    @FUNTYPE
    def fun():
        return u'xxx'
    assert fun
