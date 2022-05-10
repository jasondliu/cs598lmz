import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with cycles, and check that gc_refs are
# updated correctly.

class A:
    pass

class B:
    pass

class C:
    pass

def check_gc_refs(l1, l2):
    l1.sort()
    l2.sort()
    assert l1 == l2

def create_cycles():
    a = A()
    b = B()
    c = C()
    a.b = b
    a.c = c
    b.a = a
    b.c = c
    c.a = a
    c.b = b
    return a, b, c

# Create a couple of cycles.
print 'creating cycles...'
a, b, c = create_cycles()

# Check gc_refs before calling gc.collect().
check_gc_refs(gc.get_referents(a), [b, c])
check_gc_refs(gc.get_referents(b), [a, c])
check_gc_refs(gc.get
