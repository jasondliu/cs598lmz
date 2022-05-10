import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable()
class N(object):
    pass
nref = weakref.ref(N())
assert gc.collectable(nref), "object still referenced"
nref=None
assert not gc.collectable(nref), "ref should not be collectable"
nref=N()
del nref
import time
time.sleep(3)
assert gc.collectable(nref), "object not collectable"
print "OK"
"""

# Test gc.is_tracked()
print >>MyStderr, "Test gc.is_tracked() specific case:"
# Test gc.is_tracked()

# XXX Should find a list of all the parameter types that is_tracked()
# should succeed for.
# (Invoking it for non-types should probably be made illegal, or at
#  least lead to "should not happen" style assertions)
class C(object):
    pass
c = C()
assert gc.is_tracked(1)
assert not gc.is_tracked(1L)
assert not gc.is
