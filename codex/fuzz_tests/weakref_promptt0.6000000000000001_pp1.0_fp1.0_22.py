import weakref
# Test weakref.ref()'s handling of classes.

class C(object):
    pass

class D(C):
    pass

c = C()
c.d = D()

ref = weakref.ref(c)
assert ref().d.__class__ is D

ref = weakref.ref(c.d)
assert ref().__class__ is D

ref = weakref.ref(D())
assert ref().__class__ is D

ref = weakref.ref(D)
assert ref().__name__ == 'D'
