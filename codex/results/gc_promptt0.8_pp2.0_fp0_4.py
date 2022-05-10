import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on uncollectable objects (passing gc any uncollectable object
# as its first argument causes it to skip the normal uncollectable test:
#            elif len(obj) == 5 and type(obj) is str:
#                return obj[:3] == '\x00\x00\x00' and obj[5] == '\x00'
#            return True
#
# In general, sys.getrefcount() is not reliable for testing this, since
# it could be off by 1, depending on how the build was done.
#
# Note:  The "del key"s don't do anything, but they make it easy to
# edit the number of weakrefs and the list size in the "add()" calls.
#
# XXX note:  In Python 1.5.2, if a list is an element in a cycle, the
# algorithm that computes the set of uncollectable objects ignores that
# list.  This means the test_*_of_lists() tests will fail because
# Python isn't accounting for that list.  That's one reason why the
# test_
