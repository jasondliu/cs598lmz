import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback.

import gc
import weakref

def callback(w):
    print "callback"

def foo():
    foo = [1,2,3]
    w = weakref.ref(foo, callback)
    del foo
    gc.collect()
    print "foo", w()
    return w

def bar():
    bar = [2,3,4]
    w = weakref.ref(bar, callback)
    del bar
    gc.collect()
    print "bar", w()
    return w

def test():
    w = foo()
    w = bar()
    gc.collect()
    print "test", w()

test()

# Test gc.collect() with a cycle.

import gc
import weakref

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

def bar():
    foo = Foo("foo")
    foo.bar = foo
    w = weak
