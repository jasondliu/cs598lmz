import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a cyclic trashcan.
# Note that all elements of the trashcan need to be collectable.

class C:
    pass

class B:
    pass

class A:
    pass

class H(object):
    def __init__(self, r):
        self.r = r

def foo2(x):
    A()
    B()
    C()
    H(x)

def foo1(i):
    foo2(weakref.ref(i))

def foo0():
    for i in range(10):
        foo1(i)
    gc.collect()

foo0()
gc.collect()
print('gc.garbage:', len(gc.garbage))
