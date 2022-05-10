import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs.

class Foo:
    pass

def test(level):
    f = Foo()
    w = weakref.ref(f)
    del f
    gc.collect(level)
    print w()
    print gc.collect(level)

test(0)
test(1)
test(2)

# Reference counting:
#    a strong reference from the locals to f
#    a strong reference from the list to f
#    a weak reference from w to f (w is in locals)
#    a strong reference from f to Foo (f is in list)
#    a strong reference from Foo to its instance dictionary
#    a strong reference from the instance dictionary to f (as __weakref__)

# In addition, the instance dictionary has a strong reference to w.
# However, this is not relevant for the test.

# This should result in the following garbage:
#    f
#    the instance dictionary of f
#    the class dictionary of Foo
#    Foo
#    the reference from the instance dictionary to f

# Level 0 collects only the
