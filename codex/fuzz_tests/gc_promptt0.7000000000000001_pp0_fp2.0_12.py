import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class Test(object):
    def __init__(self, *args):
        self.args = args
    def __del__(self):
        gc.collect()

def test_fn(a, b, c):
    x = Test(a, b, c)
    gc.collect()
    y = Test(a, b, c)
    gc.collect()
    z = Test(a, b, c)
    gc.collect()
    return x, y, z

x, y, z = test_fn(1, 2, 3)
# Test gc.garbage
class Test(object):
    def __init__(self, *args):
        self.args = args
    def __del__(self):
        print gc.garbage

def test_fn(a, b, c):
    x = Test(a, b, c)
    y = Test(a, b, c)
    z = Test(a, b, c)
    return x, y, z

x, y, z = test_
