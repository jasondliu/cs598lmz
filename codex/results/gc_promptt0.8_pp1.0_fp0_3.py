import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
class Foo(object):
    def __del__(self):
        print "Deleted"
        global deleted
        deleted = True
        gc.collect()
        del deleted

f = Foo()
del f
for i in range(1000):
    Foo()
    del f
del f
gc.collect()
f = Foo()
f.bar = f
del f
gc.collect()
Foo()
gc.collect()

# Test del triggered collection
del deleted
class Foo(object):
    def __del__(self):
        print "Deleted"
        global deleted
        deleted = True
        del x
        gc.collect()
        del deleted

f = Foo()
del f
gc.collect()
del deleted

class Foo(int):
    def __del__(self):
        global deleted
        deleted = True

f = Foo()
del f
for i in range(1000):
    Foo()
    del f
del f
gc.collect()
f = Foo()
f.bar = weakref.ref(f)
del f

