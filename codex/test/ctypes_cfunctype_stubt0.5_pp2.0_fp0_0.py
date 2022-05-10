import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def fun2():
    return "world"

print(fun())
print(fun2())

class C(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "C(%r, %r)" % (self.x, self.y)

print(C(1, 2))
print(C(1, y=2))
print(C(y=2, x=1))

def f(x, y, *args, **kwargs):
    print(x, y, args, kwargs)

f(1, 2)
f(1, 2, 3, 4, 5)
f(1, 2, 3, 4, 5, z=6, w=7)

class C(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
