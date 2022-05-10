import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    def __del__(self):
        print "Foo deleted"

def bar():
    print "bar() called"

f = Foo()
wr = weakref.ref(f, bar)
print "created ref", wr
del f
print "del f"
print "created ref", wr
print "calling gc.collect()"
gc.collect()
print "created ref", wr
print "calling gc.collect()"
gc.collect()
print "created ref", wr
