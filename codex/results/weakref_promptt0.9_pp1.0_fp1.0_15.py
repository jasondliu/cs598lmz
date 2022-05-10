import weakref
# Test weakref.ref on some classes.

class A(object):
    pass


a = A()
r = weakref.ref(a)
a2 = r()
assert a is a2
a = 0
assert r() is None

class B(object):

    def __init__(self, obj):
        self.obj = obj


b = B(A())
r = weakref.ref(b)
b2 = r()
print b2
assert b is b2
b = 0
assert r() is None
b2.obj = 0
assert r().obj is None

class C(object):

    def __init__(self, obj):
        self.obj = list(obj)


c = C((A(), A()))
r = weakref.ref(c)

c2 = r()
assert c is c2
c = 0
assert r() is None
c2.obj[0] = 0
print r().obj
assert r().obj[0] is None
del c2.obj
assert r() is None

class D(object):
    pass


