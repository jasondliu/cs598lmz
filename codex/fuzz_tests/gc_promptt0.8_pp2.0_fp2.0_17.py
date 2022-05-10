import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on an unreachable container object.
import gc, sys
def bar():
    class A:
        pass
    a = A()
    a.b = A()
    a.b.a = a
sys.stdout.flush()
gc.collect()
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
# Test gc.collect() on an uncollectable container object.
gc.collect()
def foo():
    class A:
        pass
    a = A()
    a.b = A()
    a.b.a = a
    wr = weakref.ref(a)
    del a
    gc.collect()
    return wr
wr = foo()
gc.collect()
print(wr())
gc.collect()
# Verify that gc.get_debug() returns the correct value.
print(gc.get_debug())
gc.set_debug(0)
print(gc.get_debug())
print(gc.get_count())
gc.collect()
print(gc.get_count())
gc.set_debug(gc.
