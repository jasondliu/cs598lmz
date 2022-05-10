import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_fun():
    assert fun() == 1

def test_fun_call():
    assert fun()() == 1

# ____________________________________________________________

class A(object):
    def __init__(self, x):
        self.x = x

def test_new():
    a = A(1)
    assert a.x == 1

def test_new_call():
    a = A(1)()
    assert a.x == 1

# ____________________________________________________________

class B(object):
    def __init__(self, x):
        self.x = x
    def __call__(self):
        return self.x

def test_call():
    b = B(1)
    assert b() == 1

def test_call_call():
    b = B(1)()
    assert b() == 1

# ____________________________________________________________

class C(object):
    def __init__(self, x):
        self.x = x
    def __call__(self):
        return self.
