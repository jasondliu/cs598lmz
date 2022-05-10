import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with weakrefs in a cycle.

class Foo(object):
    pass

class Bar(object):
    pass

# Create a cycle with two weakrefs.
f = Foo()
b = Bar()
f.b = b
b.f = f

fwr = weakref.ref(f)
bwr = weakref.ref(b)

del f
del b

# Check that we are in the cycle.
gc.collect()
assert fwr() is not None
assert bwr() is not None

# Break the cycle by deleting one of the weakrefs.
del bwr
gc.collect()

# Check that we are no longer in the cycle.
assert fwr() is None
assert bwr() is None

# Check that we are not leaking a persistent object.
del fwr
for i in range(10):
    gc.collect()
print [x for x in gc.garbage if type(x) is weakref.ReferenceType]
assert not [x for x in gc.garbage if type(x) is weakref.ReferenceType
