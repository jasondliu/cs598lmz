import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class C:
    def __init__(self, n):
        self.n = n
    def __repr__(self):
        return "<C %s>" % self.n

# Create a reference cycle
c1 = C(1)
c2 = C(2)
c1.cycle = c2
c2.cycle = c1

print gc.collect()
print gc.garbage
del c1, c2
print gc.collect()
print gc.garbage

# Create a reference cycle
c1 = C(1)
c2 = C(2)
c1.cycle = c2
c2.cycle = c1

# Break the reference cycle
wr = weakref.ref(c1)
del c1, c2

print gc.collect()
print gc.garbage
print wr()
print gc.collect()
print gc.garbage
print wr()

# Create a reference cycle
c1 = C(1)
c2 = C(2)
c1.cycle = c2
c
