import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    pass

def bar():
    f = Foo()
    f.x = f

bar()
gc.collect()

# Test gc.get_referrers()

class Foo(object):
    pass

def bar():
    f = Foo()
    f.x = f

bar()
gc.collect()

# Test gc.get_referents()

class Foo(object):
    pass

def bar():
    f = Foo()
    f.x = f

bar()
gc.collect()

# Test gc.get_objects()

class Foo(object):
    pass

def bar():
    f = Foo()
    f.x = f

bar()
gc.collect()

# Test gc.get_stats()

class Foo(object):
    pass

def bar():
    f = Foo()
    f.x = f

bar()
gc.collect()

# Test gc.is_tracked()

class Foo(object):
   
