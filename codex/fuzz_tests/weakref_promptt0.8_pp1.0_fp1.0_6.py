import weakref
# Test weakref.ref for iterating through all referenced objects
# and for allowing them to be garbage collected.

import weakref
import gc

# create a reference cycle
a = []
b = [a]
a.append(b)

# create a weak reference to the list object
r = weakref.ref(a)

# test that the list object can be accessed via the weak reference
assert r() is a

# test that the list object is still alive
assert a is not None

# remove all references to the list object
del a
del b
assert r() is None

# create a reference cycle
class A: pass
class B: pass
a = A()
b = B()
a.next = b
b.next = a

# create a weak reference to the instance
r = weakref.ref(b)

# create a circular list of the weak references
w = []
w.append(r)

# check that the circular list of weak references does not create
# reference cycles
gc.collect()
assert gc.collect() == 0

# check that the weak references can still
