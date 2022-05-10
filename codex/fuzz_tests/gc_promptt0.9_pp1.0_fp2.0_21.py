import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect.  It returns the number of objects collected and
# deallocated.
eq(gc.collect(), 17)  # XXX

# Test the garbage that is left behind.  This garbage *should* be cyclic,
# so gc.collect() won't really collect it.
eq(gc.collect(), 0)  # XXX

# XXX
# The following collection is NOT guaranteed to collect everything.
# We'll do it twice and hope that we get it all.
gc.collect()
gc.collect()

# There should be at least these many objects still left.  We rely on
# the invariant that non-finalizer-objects are collected before, i.e.
# all objects here are finalizer objects.  In CPython 2.4, those are
# the only objects still left.
# XXX
eq(gc.collect(), 8)  # XXX

del n

# n is now an uncollectable, unreachable gc.NonCollectable instance
class C(gc.Collectable):
    pass
if verbose:
    print '(not) creating heap-cycles including uncollectable'
x
