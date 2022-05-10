import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with uncollectable cycles

def setUp(self):
    self.one = one = []
    self.two = two = []
    self.one.append(two)
    self.two.append(one)

def test(self):
    one = self.one
    two = self.two
    del self.one, self.two
    one = two = None
    gc.collect()
    gc.set_debug(gc.DEBUG_COLLECTABLE)



if __name__ == '__main__':
    test(None)
