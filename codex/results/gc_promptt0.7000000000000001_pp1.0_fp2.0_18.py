import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect_generations().
# Create a cycle, collect it, and verify that only the last generation
# was collected.

gc.collect_generations()

class A(object):
    pass

def f():
    a = A()
    a.b = A()
    a.b.a = a

f()
f()

weak_a = weakref.ref(f.func_closure[2].cell_contents)

assert weak_a() is not None
gc.collect()
assert weak_a() is not None
gc.collect_generations(0)
assert weak_a() is None
