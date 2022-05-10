import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

# The following tests gc.collect() by tracking a weak
# reference to an object.  If the object is collected,
# then the weak reference is set to None.  If the weak
# reference is not set to None, then the object is not
# collected.

# The weak reference is checked after gc.collect() is
# called.  The check is performed in a loop because
# of the possibility that gc.collect() may be a no-op.

def check(test, result, collectable):
    if collectable:
        if result is not None:
            print(test, "failed!")
            print("Object was not collected.")
            print("Weak reference still points to object.")
    else:
        if result is None:
            print(test, "failed!")
            print("Object was collected.")
            print("Weak reference does not point to object.")

# Test gc.collect() with a single object.

def test1():
    print("Test1:", end=' ')
    class C:
        pass
    c = C()
    w
