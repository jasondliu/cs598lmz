import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref enabled

import gc
import weakref

class Foo(object):
    pass

class Bar(object):
    pass

def counts():
    print 'collectable =', len(gc.collect())

x = Foo()
y = Foo()

counts()

# Create a cycle
x.foo = y
y.foo = x
del y

counts()

# Break the cycle
x.foo = None

counts()

# Create a different cycle
x.foo = Bar()
x.foo.foo = x.foo

counts()

# Break the cycle
x.foo = None
del x

counts()

# Create a different cycle
x = Foo()
x.foo = Foo()
x.foo.foo = x.foo

counts()

# Break the cycle
x.foo.foo = None
x.foo = None
del x

counts()

# Create a different cycle
x = Foo()
x.foo = Bar()
x.foo.foo = x.foo


