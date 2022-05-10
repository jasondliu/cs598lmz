import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with uncollectable cycles
class MyClass:
    pass

p1 = MyClass()
p2 = MyClass()
p1.p = p2
p2.p = p1


def fun():
    return p1
a = fun()

fun1 = fun
fun2 = fun
wref = weakref.ref(fun)
del fun

gc.collect()
print(gc.garbage)
print(gc.collect())
print(gc.garbage)
fr = wref()
print(fr)
fr = wref()
print(fr)
del fr, fr2
print(gc.garbage)
assert not gc.garbage, gc.garbage
gc.collect()
assert not gc.garbage, gc.garbage
# Bug of 2.4: using gc.DEBUG_SAVEALL, we could find the function.  That's wrong
# --- this is an uncollectable cycle.

gc.garbage.remove(p1)
del p1, p2
