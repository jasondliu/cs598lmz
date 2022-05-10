import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
# Test gc.collect(2)
# Test gc.collect(1)
def callback(wr):
    print "collected %s" % wr
#gc.set_debug(gc.DEBUG_LEAK)
#gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
#gc.set_debug(gc.DEBUG_SAVEALL)
gc.set_debug(gc.DEBUG_STATS)
a = []
for i in range(10):
    a.append(weakref.ref(object(), callback))

print a
del a
print "collecting"
gc.collect()
