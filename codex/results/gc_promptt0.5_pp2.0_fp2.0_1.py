import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    def __init__(self, name):
        self.name = name

def f():
    a = A("a")
    wr = weakref.ref(a)
    del a
    print wr() is None
    gc.collect()
    print wr() is None

f()
f()
