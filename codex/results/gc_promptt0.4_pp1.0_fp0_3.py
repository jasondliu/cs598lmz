import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Test:
    def __init__(self):
        self.data = [1, 2, 3, 4]
        self.child = TestChild()
        self.child.parent = self

class TestChild:
    def __init__(self):
        self.parent = None

def test():
    t = Test()
    wr = weakref.ref(t)
    del t
    gc.collect()
    assert wr() is None

test()
# Test gc.get_objects()

def test():
    import gc
    l = []
    l.append(l)
    gc.collect()
    l2 = gc.get_objects()
    assert l in l2
    assert l2.count(l) == 1
    l.append(l)
    gc.collect()
    l2 = gc.get_objects()
    assert l in l2
    assert l2.count(l) == 2

test()
# Test gc.get_referrers()

def test():
    import
