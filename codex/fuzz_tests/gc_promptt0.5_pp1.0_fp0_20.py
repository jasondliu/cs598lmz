import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

class E:
    pass

for c in [A, B, C, D, E]:
    print 'testing class', c.__name__
    x = c()
    xref = weakref.ref(x)
    print '    id(x) =', id(x)
    print '    xref() is x:', xref() is x
    del x
    gc.collect()
    print '    xref() is now:', xref()
    print

# Test gc.is_tracked()
print "gc.is_tracked(x) =", gc.is_tracked(x)
print "gc.is_tracked(xref) =", gc.is_tracked(xref)

# Test gc.get_referrers()
print "gc.get_referrers(x) =", gc.get
