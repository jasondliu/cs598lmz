import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This test makes sure gc.collect() collects objects that are collectable
# but not yet tracked by the garbage collector.
#
# Objects are considered garbage collectable when they are unreachable but
# also have a __del__() method.
#
# The test creates a reference cycle, makes an object participating in the
# reference cycle garbage collectable, verifies that gc.collect() doesn't
# collect it, then breaks the reference cycle.  After that gc.collect() is
# expected to collect the object.
# This test makes sure gc.collect() collects objects that are collectable
# but not yet tracked by the garbage collector.
#
# Objects are considered garbage collectable when they are unreachable but
# also have a __del__() method.
#
# The test creates a reference cycle, makes an object participating in the
# reference cycle garbage collectable, verifies that gc.collect() doesn't
# collect it, then breaks the reference cycle.  After that gc.collect() is
# expected to collect the object.

class DelMe:
    def __del__(self):

