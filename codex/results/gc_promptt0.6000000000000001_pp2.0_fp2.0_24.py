import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with weakrefs.

# Create a bunch of cyclic garbage
class A:
    pass

def callback(x):
    print("callback", x)

def callback2(x):
    print("callback2", x)

# Create a bunch of cyclic garbage
class A:
    pass

for i in range(10):
    a = A()
    w = weakref.ref(a, callback)
    w2 = weakref.ref(a, callback2)
    del a

del w, w2

# Collect everything reachable from the global namespace.
gc.collect()

# Print all objects still alive.
print("\nGarbage:")
for x in gc.garbage:
    s = str(x)
    if len(s) > 77:
        s = s[:73]+"..."
    print(type(x), "\n  ", s)
