import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    pass

class Bar(object):
    pass

def func():
    f = Foo()
    b = Bar()
    f.b = b
    b.f = f
    return f

f = func()
f = None
gc.collect()

# Test gc.get_referrers()

def func():
    f = Foo()
    b = Bar()
    f.b = b
    b.f = f
    return f

f = func()
r = gc.get_referrers(f)
assert r[0] is f.b
assert r[1] is f
assert r[2] is globals()

f = None
gc.collect()

# Test gc.get_referents()

def func():
    f = Foo()
    b = Bar()
    f.b = b
    b.f = f
    return f

f = func()
r = gc.get_referents(f)
assert r[0] is f.b
