import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on weakrefs that are not bound,
# but are part of the items of dictionaries.
#
# By Martin von Loewis, with modifications by Tim Peters

# In Python 2.3, gc and weakref were each internally optimized
# in multiple ways with the effect of breaking other optimizations
# in the other module.  The net effect was that this test was
# supposed to succeed (and did not), but it only revealed the bug
# because of a random coincidence.
#
# In Python 2.4 and later, those problems were fixed, but the test
# still failed because it didn't account for an optimization in
# 2.4.  For example, when a weakref list was cleared, it was not
# re-investigated for new collectable objects until it was resized.
# Consequently, the test's failure was very timing-dependant.
# This bug in the test has been fixed for 2.4 as well.

# The threshold for calling collect is usually 2; it doubles each time
# collect is called within a certain window.  That's a problem here,
# since the test is too fast.  Force
