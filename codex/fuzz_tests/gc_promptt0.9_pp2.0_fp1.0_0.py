import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs and finalization

class Foo:
    def __del__(self):
        L.append(self)

def f(n):
    for i in range(n):
        Foo()


# Create lots of new objects to make at least 2 generations
f(100)
L = []
# Collect from generation 1
gc.collect(1)
assert L == []
# Create lots more objects to move the previous objects to
# generation 2
f(100)
gc.collect(2)
# Check that objects in generation 2 are collected
# (due to weakrefs in the finalizers of generation 1 objects)
assert L == []

# Repeat the test, but put the weakrefs in objects in the
# youngest generation (the generation 1 objects created
# above)
class Foo:
    def __del__(self):
        L.append(wr)

def g(n):
    for i in range(n):
        Foo()

# Record weakrefs to the generation 1 objects
wr = []
for i in range(100):
    wr.append(weakref
