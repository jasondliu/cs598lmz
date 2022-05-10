import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return (1,2,3)

class A(object):
    def __init__(self):
        self.x = 1
    def __repr__(self):
        return "<A object>"

@FUNTYPE
def fun2():
    return A()

def test_p_float():
    import sys
    class float(object):
        def __init__(self, value):
            self.value = value
        def __float__(self):
            return self.value
    a = float(1)
    assert sys.platform == 'win32' or type(p_float(a)) is float

def test_py_object():
    assert py_object(0) == 0
    assert py_object(0.0) == 0.0
    assert py_object(None) is None
    assert py_object(False) is False
    assert py_object(True) is True

def test_py_object_ref():
    a = A()
    ref = py_object_ref(a)
    assert repr(ref).startswith('
