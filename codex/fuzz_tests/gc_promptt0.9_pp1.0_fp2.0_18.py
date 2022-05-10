import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
gc.collect() # force collection of generation 1

class X(object):
    pass

class A(X):
    def __init__(self, count):
        self.doorbell = ResultCallback()
        self.stuff = [X() for i in xrange(count)]
        self.morestuff = [X() for i in xrange(count)]

    def callback(self, *args):
        pass

x = weakref.proxy(X())
a = A(5000)
a.doorbell.callback = a.callback
del a
x = weakref.proxy(X())
gc.collect()
if gc.collect():
    print "collectable"
gc.set_debug(0)
