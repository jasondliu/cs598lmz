import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect and gc.get_referrers (which is not available in
# debug mode).
class A:
    pass

a = A()
# We use a weakref to avoid keeping a reference to a in the frame.
# Otherwise, the gc wouldn't collect a, and the test would fail.
class B(object):
    def __init__(self, a):
        self.a = weakref.ref(a)

    def get_ref(self):
        return self.a

b = B(a)
del a
# At this point, b is the only reference to a.  It's a weak reference, so a
# will be collected.  b.__dict__ is the only container that holds a reference
# to b.a.
gc.collect()
# b.a is still alive
assert b.get_ref()() is not None
# b.a is still alive
assert b.get_ref()() is not None
# Now we delete b, so a has no more references.
del b
gc.collect()
# Now a is collected.
assert gc.collect
