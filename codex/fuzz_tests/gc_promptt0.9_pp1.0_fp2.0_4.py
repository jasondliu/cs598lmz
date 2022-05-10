import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect (Issue #3165)

class C:
    pass

c_refs = weakref.WeakValueDictionary()

def test(x):
    print("STARTING TEST", x)
    for j in range(2):
        for i in range(x):
            a = C()
            c_refs.update({id(a):a})
            a = None
        del a
        gc.collect()
        print("GC DONE", c_refs)
    print("END TEST")

# This will always leak a few objects, and is checked in test_weakref.
test(10)

# This should clean up all objects.
test(100)

# This should clean up all objects.
for i in range(5):
    test(10)
    gc.collect()
