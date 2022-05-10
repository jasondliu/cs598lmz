import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

class C:
    pass

# Create a reference cycle
c1 = C()
c2 = C()
c1.cycle = c2
c2.cycle = c1

print(gc.collect())

assert gc.collect() == 2

del c1, c2
print(gc.collect())

# Create a reference cycle
c1 = C()
c2 = C()
c1.cycle = c2
c2.cycle = c1

# Create a reference to the cycle
r = weakref.ref(c1)

print(gc.collect())
print(r())
