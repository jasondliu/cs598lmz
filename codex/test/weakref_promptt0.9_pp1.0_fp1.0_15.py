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
