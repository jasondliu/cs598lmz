import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Test(object):
    def __init__(self, *args):
        self.args = args

def test(n):
    # Create a cycle
    t = Test()
    t.a = t
    t.b = Test()
    t.b.a = t.b
    t.b.b = t
    t.b.c = Test()
    t.b.c.a = t.b.c
    t.b.c.b = t.b
    t.b.c.c = t

    # Create a ref to the test object
    ref = weakref.ref(t)

    # Create a list of n test objects, with a ref to each one
    list = [Test() for i in range(n)]
    list[0] = t
    list[-1].a = list[0]
    list[-1].b = list[-2]
    list[-1].c = list[-3]
    refs = [weakref.ref(obj) for obj in list]

    # Now delete everything
