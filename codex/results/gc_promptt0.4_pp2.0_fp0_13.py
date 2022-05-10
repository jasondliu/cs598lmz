import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    pass

class Bar(object):
    pass

f = Foo()
b = Bar()

# create a reference cycle
f.x = b
b.x = f

# a list that contains the objects
l = [f, b]

# a weak reference to f
wf = weakref.ref(f)

# a weak reference to b
wb = weakref.ref(b)

print 'Before:', wf(), wb()

# remove the last reference to f and b
del l

# force a collection
gc.collect()

print 'After:', wf(), wb()

# Test gc.garbage

class Foo(object):
    def __init__(self, x):
        self.x = x

class Bar(object):
    def __init__(self, x):
        self.x = x

f = Foo(1)
b = Bar(2)

# create a reference cycle
f.x = b
b.x = f

# a list that
