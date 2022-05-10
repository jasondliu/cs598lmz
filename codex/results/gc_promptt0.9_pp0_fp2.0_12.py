import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() without arguments
gc.collect()

class Foo(object):
    def __init__(self, x):
        self.x = x

    def __del__(self):
        print "Foo, going away, x =", self.x

assert(gc.collect() == 0)

f = Foo(1)
f_wr = weakref.ref(f)
f = None
assert(gc.collect() == 0)

f = Foo(2)
f = None
assert(gc.collect() == 1)

assert gc.collect() == 0

refs = [weakref.ref(Foo(i)) for i in range(1000)]
refs[10]
del refs
assert gc.collect() == 1000
