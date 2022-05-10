import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%s)' % self.name

f = Foo('a')
f2 = Foo('b')
f2.cycle = f
f.cycle = f2
f2 = None
f = None
gc.collect()
# Test weakref.finalize()
class Foo:
    def __del__(self):
        print('deleted!')

f = weakref.finalize(Foo(), lambda: print('finalized!'))
f()
f.alive
del f
gc.collect()
