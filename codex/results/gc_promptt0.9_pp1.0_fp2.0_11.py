import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect method

class C:
    pass

o = C()
o.attr = o
r = weakref.ref(o)
o2 = C()
o2.attr = o2
r2 = weakref.ref(o2)

count = gc.collect()
assert r() is o and r2() is o2, "gc.collect didn't find collectable objects that were reachable."
assert count == 0, "gc.collect didn't return correct objects collected"

del o, o2
count = gc.collect()
assert count == 2, "gc.colect didn't collect newly unreferenced objects"

assert r() is None and r2() is None, "gc.collect didn't collect newly unreferenced objects"
# Test gc.get_referrers

# Object referrers structure

# x1 -> [x2, x3]
# x2 -> x1
# x3 -> x1


class A:
    pass
a = A()
b = A()
c = A()

a.attr = [b, c]
