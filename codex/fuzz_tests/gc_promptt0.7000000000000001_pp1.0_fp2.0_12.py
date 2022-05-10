import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() at various points

# Create a list with a reference cycle
l = [{}]
l[0][0] = l
l2 = l
del l
gc.collect()
print gc.collect()      # This should find l

# Create a cyclic tuple (just to be different)
d = {}
t = weakref.ref(d), (weakref.ref(d),)
del d
gc.collect()
print gc.collect()      # This should find t

# Create a dictionary with a reference cycle
d = {}
d[0] = d
d2 = d
del d
gc.collect()
print gc.collect()      # This should find d

# Create a cycle with functions
def f():
    def g():
        pass
    return g
f()
f2 = f()
del f
gc.collect()
print gc.collect()      # This should find f

# Create a cycle with classes
class C:
    def __init__(self, d):
        self.d = d

c = C(d2)

