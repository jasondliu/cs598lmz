import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass
a = A()
b = A()
for o in gc.get_objects():
    if type(o) is A:
        print(o)

print("\nCollecting...")
n = gc.collect()

print("\nCollecting again...")
n = gc.collect()
for o in gc.get_objects():
    if type(o) is A:
        print(o)
# Test gc.garbage
a = A()
b = A()
a.b = b
b.a = a
del a
del b
gc.collect()
print(gc.garbage)
# Test gc.get_referrers()
a = A()
b = A()
a.b = b
b.a = a
c = A()
c.a = a
c.b = b
del a, b, c
gc.collect()
print(gc.garbage)
r = gc.get_referrers(gc.garbage[0])
print(r)
#
