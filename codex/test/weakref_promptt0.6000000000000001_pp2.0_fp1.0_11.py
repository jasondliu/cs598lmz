import weakref
# Test weakref.ref for a function object
import gc
def foo():
    pass
r1 = weakref.ref(foo)
r2 = weakref.ref(foo)
del foo
gc.collect()
print(r1() is r2())
