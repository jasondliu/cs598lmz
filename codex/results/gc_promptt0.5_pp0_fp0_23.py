import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() that returns the number of collected objects.

class C:
    def __init__(self):
        self.x = 1

def test_collect():
    l = []
    for i in range(100):
        obj = C()
        l.append(weakref.ref(obj))
        obj.x = i
    del obj
    for i in range(10):
        gc.collect()
    for obj in l:
        assert obj() is not None
    for i in range(10):
        gc.collect()
    for obj in l:
        assert obj() is not None
    for i in range(10):
        gc.collect()
    for obj in l:
        assert obj() is None

test_collect()
