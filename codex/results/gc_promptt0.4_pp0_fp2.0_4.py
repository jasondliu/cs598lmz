import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs to objects that have a __del__ method.
# This used to crash Python.

class A:
    def __del__(self):
        pass

def foo():
    a = A()
    w = weakref.ref(a)
    del a
    gc.collect()

foo()
foo()
foo()

# Test that gc.collect() calls __del__ methods.

class B:
    def __del__(self):
        B.n = B.n + 1

B.n = 0
b = B()
w = weakref.ref(b)
del b
gc.collect()
assert B.n == 1

# Test that gc.collect() calls __del__ methods even if they are
# reachable via a cycle.

class C:
    def __del__(self):
        C.n = C.n + 1

C.n = 0
c1 = C()
c2 = C()
c1.cycle = c2
c2.cycle = c1
w = weakref.ref
