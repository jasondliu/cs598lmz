import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect directly with a single argument.

def debug_collect(n, verbose):
    assert gc.collect(n) > 0
    if verbose:
        print n, gc.garbage

# Create cycles involving the following objects, which are all collectable
# in generation n (even objects with __del__ are collectable as soon as their
# __del__ is unbound).
A = B = C = D = E = [1,2,3]
A = weakref.ref(A)
debug_collect(0, 1)

A = B = C = D = E = [1,2,3]
A = MyList(A)     # __del__ bound and will append self to gc.garbage
debug_collect(1, 1)
debug_collect(0, 1)

A = B = C = D = E = [1,2,3]
A = (1, MyList(A)) # __del__ bound and will append self to gc.garbage
debug_collect(1, 1)
debug_collect(0, 1)

A = B
