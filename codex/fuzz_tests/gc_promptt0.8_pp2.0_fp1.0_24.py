import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on weakref and callbacks

# Make some objects to collect
class Foo:
    def __init__(self, i):
        self.i = i
    def __del__(self):
        print 'Foo.__del__(%d)' % self.i

class Bar(object):
    def __init__(self, i):
        self.i = i
    def __del__(self):
        print 'Bar.__del__(%d)' % self.i

for i in range(10):
    globals()['f%d' % i] = Foo(i)
    globals()['b%d' % i] = Bar(10+i)

# Make a weakref object, with a callback
count = 0
def callback(wr):
    global count
    print 'callback with', wr(), count
    count += 1
class MyCallable:
    def __call__(self, wr):
        global count
        print 'callback with', wr(), count
        count += 1

def makeref(obj, callback=callback):
    if is
