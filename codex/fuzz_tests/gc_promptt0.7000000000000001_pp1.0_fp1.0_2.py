import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

def assert_refs_equal(a, b):
    if a is b:
        return
    if len(a) != len(b):
        raise AssertionError("%r != %r" % (a, b))
    for x, y in zip(a, b):
        assert x == y

class Test:
    def __init__(self, name):
        self.name = name
        self.assert_refs_equal = assert_refs_equal
    def __del__(self):
        self.assert_refs_equal(gc.garbage, [self])
        print "ok"

def f():
    x = Test("f")
    print "collecting..."
    gc.collect()
    print "done"
    x = None
    gc.collect()
    print "f is gone"
f()
print "gc.collect() is done"
gc.collect()
print "ok"

# One more test, this time with __del__.

class A:
    def __del__(self):

