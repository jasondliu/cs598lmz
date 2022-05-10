import weakref
# Test weakref.ref(1) such that the object remains alive
try:
    strongref = 1
    ref(strongref)
except TypeError:
    pass
else:
    raise TestFailed("expected TypeError")
# Test weakref.ref(class) such that the object remains alive
try:
    ref(TestClass)
except TypeError:
    pass
else:
    raise TestFailed("expected TypeError")


# Test hard reference cycles created by subtypes of weakref.finalize
# that define __del__
obj = C()
ref1 = weakref.ref(obj, callback)
ref2 = weakref.ref(obj, callback2)

if gc.collect():
    raise TestFailed("uncollectable garbage")
del obj
if gc.collect():
    if not is_gc_enabled():
        raise TestFailed("uncollectable garbage")
    else:
        # XXX do we want to raise [MemoryError] here?
        raise TestFailed("uncollectable garbage")

if callback.called:
    print("Unexpectedly called callback with finalizer subtype
