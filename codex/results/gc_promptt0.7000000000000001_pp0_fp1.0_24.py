import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback.

def callback(wr, gct):
    print('callback(%r, %r)' % (wr, gct))
    wrefs.remove(wr)

wrefs = []

class C:
    pass

for i in range(5):
    o = C()
    wr = weakref.ref(o, callback)
    wrefs.append(wr)

print(gc.collect())

print(wrefs)
