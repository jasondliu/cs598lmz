import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref to an instance
class Foo:
    def __init__(self):
        self.data = [1] * 10
def test():
    f = Foo()
    wr = weakref.ref(f)
    f.data.append(f)
    del f
    gc.collect()
    if wr() is not None:
        print('test failed!')
        print(wr())
test()

# Test gc.collect() with a weakref to a cyclic tuple
def test2():
    l = []
    for i in range(100):
        l.append((i, l))
    wr = weakref.ref(l)
    del l
    gc.collect()
    if wr() is not None:
        print('test2 failed!')
        print(wr())
test2()

# Test gc.collect() with a weakref to an instance with a custom deleter
class Foo:
    def __init__(self):
        self.data = [1] * 10
    def __del__(self):
        pass

