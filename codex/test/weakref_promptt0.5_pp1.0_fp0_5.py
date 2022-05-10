import weakref
# Test weakref.ref()
import gc

class C(object):
    pass

# Create a strong reference
obj = C()
# Create a weak reference
wref = weakref.ref(obj)
# Get the object through the weak reference
obj2 = wref()
assert obj is obj2

# Clear the strong reference
del obj
# The object still exists
assert obj2 is not None

# Clear the weak reference
del wref
# The object is still alive
assert obj2 is not None

# Clear the strong reference
obj2 = None
# The object is no longer alive
assert gc.collect() == 1

# Test weakref.proxy()
obj = C()
wref = weakref.proxy(obj)
assert isinstance(wref, weakref.ProxyType)
assert wref is obj

# Clear the strong reference
del obj
# The object is no longer alive
assert gc.collect() == 1

# Test weakref.getweakrefcount()
obj = C()
assert weakref.getweakrefcount(obj) == 0

# Create a weak reference
w
