import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect():
gc.collect()

class C(object):
    def __init__(self, a):
        self.a = a
        self.wr = weakref.ref(a)

gc.collect()

def f():
    a = C([1, 2, 3])
    b = C(a)
    b = C(a)
    b = None

f()
gc.collect()

# A cycle with objects of different types.
gc.collect()
def f():
    a = C([1, 2, 3])
    b = C(a)
    b.a = a

f()
gc.collect()

# A cycle with new-style classes.
gc.collect()
class D(object):
    def __init__(self, a):
        self.a = a
        self.wr = weakref.ref(a)

def f():
    a = D([1, 2, 3])
    b = D(a)
    b.a = a

f()
gc.collect()

print 'done'
