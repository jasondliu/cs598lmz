import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with a weak reference to an object which is not tracked
# by the garbage collector.
class A:
    pass
def f():
    a = A()
    wr = weakref.ref(a)
    del a
    gc.collect()
    return wr
wr = f()
wr()

# Test gc.collect with weakrefs to objects which are tracked by the
# garbage collector.
class A:
    pass
def f():
    a = A()
    wr = weakref.ref(a)
    del a
    gc.collect()
    return wr
wr = f()
wr()

# Test gc.collect with a weak reference to an object which is not tracked
# by the garbage collector, but which has a __del__ method.
class A:
    def __del__(self):
        pass
def f():
    a = A()
    wr = weakref.ref(a)
    del a
    gc.collect()
    return wr
wr = f()
wr()

# Test gc.collect with weakrefs to objects which are
