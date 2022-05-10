import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

def bar():
    f = Foo()
    wr = weakref.ref(f)
    del f
    return wr

wr = bar()
print(wr)
gc.collect()
print(wr)

# Test gc.get_referrers()

class Foo:
    pass

def bar():
    f = Foo()
    wr = weakref.ref(f)
    del f
    return wr

wr = bar()
print(gc.get_referrers(wr))

# Test gc.get_referents()

class Foo:
    pass

def bar():
    f = Foo()
    wr = weakref.ref(f)
    del f
    return wr

wr = bar()
print(gc.get_referents(wr))

# Test gc.get_objects()

class Foo:
    pass

def bar():
    f = Foo()
    wr = weakref.ref(f)
    del f
    return wr

wr = bar()
