import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    pass

class Bar(object):
    pass

def f():
    f1 = Foo()
    f2 = Foo()
    b = Bar()
    b.f1 = f1
    b.f2 = f2
    f1.b = b
    f2.b = b
    f1.f2 = f2
    f2.f1 = f1
    return f1

f1 = f()
f2 = f1.f2
b = f1.b

# f1, f2, b are all alive
gc.collect()

# f1, f2, b are all alive
del f1
gc.collect()

# f2, b are alive
del f2
gc.collect()

# b is alive
del b
gc.collect()

# nothing is alive

# Test gc.get_referrers()

class Foo(object):
    pass

class Bar(object):
    pass

def f():
    f1 = Foo()
    f2
