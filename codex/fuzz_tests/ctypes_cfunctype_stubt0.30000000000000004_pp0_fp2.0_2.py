import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_fun():
    assert fun() == 1

class C(object):
    @staticmethod
    def fun():
        return 1

CFUNTYPE = ctypes.CFUNTYPE(ctypes.py_object)
C.fun = CFUNTYPE(C.fun)

def test_staticmethod():
    assert C.fun() == 1

class C(object):
    @classmethod
    def fun(cls):
        return 1

CFUNTYPE = ctypes.CFUNTYPE(ctypes.py_object)
C.fun = CFUNTYPE(C.fun)

def test_classmethod():
    assert C.fun() == 1

class C(object):
    def fun(self):
        return 1

CFUNTYPE = ctypes.CFUNTYPE(ctypes.py_object, ctypes.py_object)
C.fun = CFUNTYPE(C.fun)

def test_method():
    assert C().fun() == 1

class C(object):
    def fun(self):
        return 1

