import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() to make sure it doesn't crash.
gc.collect()

class A:
    pass

a = A()
a.b = A()
a.b.a = a

ref = weakref.ref(a)
del a
gc.collect()
try:
    ref()
except ReferenceError:
    pass

# Test weakrefs to objects with __del__ methods
class C:
    def __del__(self):
        pass

c = C()
w = weakref.ref(c)
del c
gc.collect()
try:
    w()
except ReferenceError:
    pass

# Test weakrefs to objects with __del__ methods that raise exceptions
class D:
    def __del__(self):
        raise ValueError

d = D()
w = weakref.ref(d)
del d
gc.collect()
try:
    w()
except ReferenceError:
    pass

# Test weakrefs to objects with __del__ methods that create cycles
class E:
    def __init__(self, i):
        self
