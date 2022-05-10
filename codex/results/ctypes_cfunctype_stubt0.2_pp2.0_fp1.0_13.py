import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_fun():
    assert fun() == "hello"

class C(object):
    def __init__(self):
        self.x = 42

def test_instancemethod():
    c = C()
    assert c.x == 42
    assert C.__init__.__get__(c) is c.__init__
    assert C.__init__.__get__(c, C) is c.__init__
    assert C.__init__.__get__(None, C) is C.__init__
    assert C.__init__.__get__(c, None) is c.__init__
    raises(TypeError, "C.__init__.__get__(c, 42)")
    raises(TypeError, "C.__init__.__get__(42)")
    raises(TypeError, "C.__init__.__get__(42, 42)")
    raises(TypeError, "C.__init__.__get__(42, c)")
    raises(TypeError, "C
