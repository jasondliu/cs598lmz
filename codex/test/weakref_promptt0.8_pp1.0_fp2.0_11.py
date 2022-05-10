import weakref
# Test weakref.ref on old-style classes
class A:
    pass
a1 = A()
a2 = A()

r = weakref.ref(a1)
assert r() is a1

r = weakref.ref(a2, lambda : None)
assert r() is a2
r = weakref.ref(a1)
assert r() is a1
# Test weakref.ref on new-style classes
class A(object):
    pass
a1 = A()
a2 = A()

r = weakref.ref(a1)
assert r() is a1

r = weakref.ref(a2, lambda : None)
assert r() is a2
r = weakref.ref(a1)
assert r() is a1
# Test weakref.proxy
p1 = weakref.proxy(a1)
assert p1 is a1
assert p1.__class__ is A

p2 = weakref.proxy(a1, lambda : None)
assert p2 is a1
assert p2.__class__ is A
