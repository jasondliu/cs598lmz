import weakref
# Test weakref.reference.
try:
    weakref.reference
except AttributeError:
    print("SKIP")
    raise SystemExit

import gc

class A:
    pass

a = A()

# Create a weak reference to A, then delete it from locals() and from the
# namespace of the class.
a_wr = weakref.ref(a)
del A.a
del a

# Delete the reference to A, then do a full GC.
elems = gc.collect()
# Check that the weak reference has been collected, and that A has also been
# collected.
print(elems == 2)
print(a_wr() is None)

# Create a second weak reference to A.
A.a_wr2 = a_wr

# Force a full GC.
elems = gc.collect()
# Check that the weak reference has not been collected.
print(elems == 0)
print(a_wr() is None)

# Delete the weak reference from the namespace.
del A.a_wr2

# Force a full GC.
elems
