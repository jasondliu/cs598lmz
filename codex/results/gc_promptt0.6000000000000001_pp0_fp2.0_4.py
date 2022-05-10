import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() not crashing
class Test:
    pass
t1 = Test()
t2 = Test()
t1.x = weakref.ref(t2)
t2.x = weakref.ref(t1)
del t1, t2
gc.collect()

# Test gc.collect() not leaking
def f():
    pass
for i in xrange(1000):
    f()
    f = lambda: None
    gc.collect()

# Test gc.collect() not leaking
class A:
    def __del__(self):
        f = lambda: None
        gc.collect()
for i in xrange(1000):
    A()
    gc.collect()

# Test gc.get_objects() not leaking
def f():
    pass
for i in xrange(1000):
    f()
    f = lambda: None
    gc.get_objects()

# Test gc.get_objects() not leaking
class A:
    def __del__(self):
        f = lambda: None
        gc.get_objects
