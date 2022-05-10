import weakref
# Test weakref.ref
import operator

class C(object):
    pass

o = C()
r = weakref.ref(o)
assert r() is o
o2 = C()
r2 = weakref.ref(o2)
assert r2() is o2

# test basic ref-like behavior
o3 = C()
r3 = weakref.ref(o3)
assert r3() is o3
del o3
assert r3() is None, "deleted object should return None from ref()"

# test that ref doesn't keep the object alive
def f():
    a = C()
    b = weakref.ref(a)
    return b

r = f()
assert r() is None

def f():
    a = C()
    b = weakref.ref(a)
    return a

r = f()
assert r is None

# test that refs return None when the object has been gc'd
# before the ref is created
def f():
    l = []
    l.append(C())
