import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect_generations
for i in range(5):
    l = [i]
    l[0] += 1
    l = [l]

gc.collect_generations()

gc.set_debug(gc.DEBUG_LEAK)
gc.collect()
print '%d objects left' % len(gc.garbage)
def callback(wr):
    print 'callback called'
    raise Exception

for i in range(10):
    weakref.ref(gc.garbage[-1], callback)
    gc.collect()

for i in range(10):
    weakref.ref(gc.garbage[-1], callback)
    gc.collect(2)

for i in range(10):
    weakref.ref(gc.garbage[-1], callback)
    gc.collect(1)

for i in range(10):
    weakref.ref(gc.garbage[-1], callback)
    gc.collect(0)
# Test gc.set_threshold
gc.collect()
print '%d objects left
