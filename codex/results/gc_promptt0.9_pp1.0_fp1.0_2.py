import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect and __del__ interactions

class C(object):
    __slots__ = ["a"]
    instances = 0
    def __init__(self, a):
        self.a = a
        type(self).instances += 1
    def __del__(self):
        type(self).instances -= 1


for cls in (C, type("D", (object,), dict(__slots__ = ["a"], instances = 0))):
    gc.collect()
    assert cls.instances == 0, cls.instances
    c1 = cls(1); c2 = cls(2)
    # Make sure gc.collect doesn't remove a live object referenced from a
    # unreachable weak reference
    c1_wr = weakref.ref(c1)
    del c1
    gc.collect()
    assert c1_wr() is not None, c1_wr
    assert cls.instances == 2, cls.instances
    del c2
    gc.collect()
    assert cls.instances == 1, cl
