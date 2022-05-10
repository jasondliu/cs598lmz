import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback

class Foo:
    def __init__(self, i):
        self.i = i
        self.wr = weakref.ref(self, self.callback)

    def callback(self, wr):
        print "callback called"
        print wr is self.wr

f = Foo(1)
f.wr()
f.wr() is f
del f
gc.collect()

# Test gc.collect() with a weakref callback that raises an exception

class Foo:
    def __init__(self, i):
        self.i = i
        self.wr = weakref.ref(self, self.callback)

    def callback(self, wr):
        print "callback called"
        print wr is self.wr
        raise ValueError

f = Foo(1)
f.wr()
f.wr() is f
del f
gc.collect()

# Test gc.collect() with a weakref callback that raises an exception
# and with a weakref that is part of a cycle

class Foo:
    def __init__
