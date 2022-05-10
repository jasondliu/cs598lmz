import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakref
# gc.collect() will collect unreachable objects marked with gc.GC_COLLECTABLE
# and make together a list of weakref callbacks to call.
# gc.collect() will return the number of unreachable objects collected.

class Foo(object):

    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return 'Foo(%d)' % self.i

    def __del__(self):
        print 'deleting', self

def callback(r):
    global callback_done
    assert not callback_done
    callback_done = True
    print 'callback(%r)' % (r,)

callback_done = False

for i in range(3):
    Foo(i)

# Check that no object collects itself while clearing a weakref
f1 = Foo(1)
ref1 = weakref.ref(f1, callback)
r1 = ref1()
f1.r1 = r1

# Make a list that contains itself
L = [Foo(
