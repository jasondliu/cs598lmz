import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def test_fun():
    assert fun() == 42

def test_fun_return_none():
    @FUNTYPE
    def fun():
        return None
    assert fun() is None

def test_fun_return_int():
    @FUNTYPE
    def fun():
        return 42
    assert fun() == 42

def test_fun_return_float():
    @FUNTYPE
    def fun():
        return 3.14
    assert fun() == 3.14

def test_fun_return_string():
    @FUNTYPE
    def fun():
        return "hello"
    assert fun() == "hello"

def test_fun_return_unicode():
    @FUNTYPE
    def fun():
        return u"hello"
    assert fun() == u"hello"

def test_fun_return_tuple():
    @FUNTYPE
    def fun():
        return (1, 2, 3)
    assert fun() == (1, 2, 3)

def test_fun_return_list():
    @FUNTYPE
   
