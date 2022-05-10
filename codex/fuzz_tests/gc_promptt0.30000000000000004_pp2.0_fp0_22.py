import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    pass

def bar():
    a = Foo()
    b = Foo()
    a.x = b
    b.x = a
    del a
    del b

bar()
gc.collect()

# Test gc.get_objects()

class Foo(object):
    pass

def bar():
    a = Foo()
    b = Foo()
    a.x = b
    b.x = a
    del a
    del b

bar()
gc.collect()

# Test gc.get_referrers()

class Foo(object):
    pass

def bar():
    a = Foo()
    b = Foo()
    a.x = b
    b.x = a
    del a
    del b

bar()
gc.collect()

# Test gc.get_referents()

class Foo(object):
    pass

def bar():
    a = Foo()
    b = Foo()
    a.x = b
    b.x = a
   
