import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
timing("gc.collect()")
gc.collect()
def test1():
    def callback():
        pass
    wr = weakref.finalize(1, callback)
    wr2 = weakref.finalize(1, callback)

def test2():
    def callback(x):
        pass
    wr = weakref.finalize(1, callback, 2)
    wr2 = weakref.finalize(1, callback, 2)

def test3():
    def callback(x, y):
        pass
    wr = weakref.finalize(1, callback, 2, 3)
    wr2 = weakref.finalize(1, callback, 2, 3)
test1()
test2()
test3()
timing("gc.collect()")
gc.collect()
def test4(x):
    def callback(x):
        pass
    wr = weakref.finalize(1, callback, x)
    wr2 = weakref.finalize(1, callback, x)
test4(1)
test4(2)
test4(3)
