import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and del x
class Foo(object):
    pass

f = Foo()
f.x = []

f_wr = weakref.ref(f)

f = None # break cycle here

gc.collect()

del f_wr
gc.collect()
# Test cyclic reference
class Foo(object):
    pass
f = Foo()
f.x = f
f_wr = weakref.ref(f)
f = None
gc.collect()
del f_wr
gc.collect()
# Test cyclic reference + finalizer
class Foo(object):
    def __init__(self):
        self.x = self
    def __del__(self):
        self.y = 1
f = Foo()
f.x = f
f_wr = weakref.ref(f)
f = None
gc.collect()
del f_wr
gc.collect()
# Test finalizer on non-collectable object
class Foo(object):
    def __del__(self):
        self.y = 1
f = Foo()
f.x = f

