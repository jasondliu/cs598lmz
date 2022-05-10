import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect returns the correct number of objects for
# collectable objects

print "Collecting..."
print gc.collect()
print "done"

print "Collecting again..."
print gc.collect()
print "done"

class Foo:
    def __del__(self):
        pass

class Err:
    def __del__(self):
        1//0


def del_cb(o):
    print "OK"

def a():
    bar = Foo()
    bar = None
    try:
        baz = Err()
        baz = None
    except ZeroDivisionError:
        pass
    cb = weakref.ref(Foo(), del_cb)
    return cb, bar, baz

gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
gc.set_debug(gc.DEBUG_SAVEALL)

result = a()

print "Collecting..."
print gc.collect()
print "done"

print "Collecting again..."
print gc.collect()
print "done"

gc.set
