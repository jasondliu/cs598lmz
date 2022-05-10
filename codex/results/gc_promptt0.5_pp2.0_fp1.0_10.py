import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on collectable objects
def test():
    for i in xrange(100):
        x = [i]
        x = weakref.ref(x)
        x()
    gc.collect()

# Test gc.collect() on uncollectable objects
def test2():
    for i in xrange(100):
        x = [i]
        x = weakref.ref(x)
        x()
    gc.collect()
    x = [1]
    x = weakref.ref(x)
    x()
    gc.collect()

# Test gc.collect() on collectable objects with a callback
def test3():
    def callback(x):
        pass
    for i in xrange(100):
        x = [i]
        x = weakref.ref(x, callback)
        x()
    gc.collect()

# Test gc.collect() on uncollectable objects with a callback
def test4():
    def callback(x):
        pass
    for i in xrange(100):
        x = [i
