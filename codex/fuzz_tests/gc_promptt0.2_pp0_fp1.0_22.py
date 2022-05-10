import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

def callback(x):
    print "callback", x

def test(n):
    for i in range(n):
        f = Foo()
        f.x = i
        f.wr = weakref.ref(f, callback)
        del f
    gc.collect()

test(10)

# Test gc.garbage

class Foo:
    pass

def test(n):
    for i in range(n):
        f = Foo()
        f.x = i
        f.wr = weakref.ref(f)
        del f
    gc.collect()

test(10)
print gc.garbage

# Test gc.get_referrers()

class Foo:
    pass

def test(n):
    for i in range(n):
        f = Foo()
        f.x = i
        f.wr = weakref.ref(f)
        del f
    gc.collect()

test(10)
print gc.get_re
