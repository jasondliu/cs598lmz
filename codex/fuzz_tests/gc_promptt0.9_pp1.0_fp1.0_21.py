import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
# It's easy to verify that collect() clears the list since collect()
# returns them.  What we'd like to test is that gc.garbage is
# cleared.  The problem is that gc.garbage is only guaranteed to be
# cleared after a full collection has occurred, which can't be
# controlled.  So this test just verifies that it's *mostly* cleared.

# MUST be weakreffable; we're testing collection!
class C(object):
    pass

# This used to foul it up because collect() would return [d], but
# d.x would keep d alive some more.
class D(object):
    def __init__(self, num):
        l[num] = self
        l[num].x = "foo"

l = []
def f():
    l.append(C())
    l.append(C())
    l.append(D(0))
    l.append(D(1))

f()           # stuff to collect
gcl = gc.collect()     # pass #1
# In true CPython, the
