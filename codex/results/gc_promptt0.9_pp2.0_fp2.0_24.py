import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakref.ref().
class B(object):
    pass

# Objects:
# 0: A
# 1: B (preference in gc)
# 2: B-dict
# 3: cyclic dependency from A to B

# Leak the dictionary
def test1():
    print "\nTest 1:"
    a = {1:B()}
    a[2] = a
    r = weakref.ref(a)
    del a
    gc.collect()
    raw = repr(r)
    print '  weakref =', raw
    assert r() is None

# Leak a simple object
def test2():
    print "\nTest 2:"
    a = B()
    a.attr = a
    r = weakref.ref(a)
    del a
    gc.collect()
    raw = repr(r)
    print '  weakref =', raw
    assert r() is None

# Leak "B"
def test3():
    print "\nTest 3:"
    a = B()
    b = B()
