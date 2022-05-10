import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

class A(object):
    def __init__(self, x):
        self.x = x
    def getx(self):
        return self.x

a = A(42)
s = pickle.dumps(a)
a = None
b = pickle.loads(s)
assert b.getx() == 42

class B(object):
    def __init__(self, x):
        self.x = x
    def __getstate__(self):
        return self.x
    def __setstate__(self, state):
        self.x = state

b = B(42)
s = pickle.dumps(b)
b = None
c = pickle.loads(s)
assert c.x == 42

class C(object):
    def __init__(self, x):
        self.x = x
    def __reduce__(self):
        return self.__class__, (self.x,)

c = C(42)
s = pickle.dumps(c)
c =
