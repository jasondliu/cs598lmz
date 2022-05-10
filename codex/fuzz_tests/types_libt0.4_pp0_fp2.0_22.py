import types
types.MethodType(func, None, A)

# Test __get__
class B(object):
    def f(self):
        return 42

b = B()
b.f()

class C(object):
    def __get__(self, obj, objtype):
        return 42

C().__get__(None, None)
B.f = C()
b.f

# Test __set__
class D(object):
    def __set__(self, obj, val):
        obj.x = val

class E(object):
    def __init__(self):
        self.x = 0

e = E()
e.x
e.f = D()
e.f = 42
e.x

# Test __delete__
class F(object):
    def __delete__(self, obj):
        obj.x = 0

class G(object):
    def __init__(self):
        self.x = 42

g = G()
g.x
g.f = F()
del g.f
g.x
