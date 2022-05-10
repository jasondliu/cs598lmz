import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
print gc.collect()

def f():
    o = 'x'*100000
    o2 = o

f()
del f
gc.collect()

# Create a large dict, trigger gc and check that dicts are collectable
# even if they contain a finalizer able to create references
# to objects in the dict. 
total = gc.collect()

def f():
    return "1"

class C:
    f = f

def create_dict():
    d = {}
    for i in range(10000):
        d[chr(i)*10000] = i
    return d


# Disable finalizers temporarily.  This keeps objects from being 
# reachable from the finalizers of other objects.
gc.disable_finalizers() 
finalizers = {}
d = create_dict()
for i in range(10):
    finalizers[i] = weakref.finalize(i, lambda : None, d, i)
del finalizers
d2 = create_dict()

# See that create_dict() and d can be collected
