import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    pass

def foo():
    a = Foo()
    a.x = Foo()
    a.x.y = a

foo()
gc.collect()
gc.collect()
gc.collect()
del foo
gc.collect()

# Test gc.get_referents()

class Foo(object):
    pass

def foo():
    a = Foo()
    a.x = Foo()
    a.x.y = a
    return a

a = foo()

r = gc.get_referents(a)
assert len(r) == 2
assert a.x in r
assert a.x.y in r

r = gc.get_referents(a, False)
assert len(r) == 2
assert a.x in r
assert a.x.y in r

r = gc.get_referents(a, True)
assert len(r) == 1
assert a.x in r

del a
gc.collect()

a = foo()

