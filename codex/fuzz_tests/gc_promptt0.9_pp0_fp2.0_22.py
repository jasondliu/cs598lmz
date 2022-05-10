import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() without argument
print('Collectable:', gc.collect())
print('unreachable:', gc.collect())
print('uncollectable:', gc.collect())

print('Collectable:', gc.collect())
l = []
l.append(l)
wr = weakref.ref(l)
print('unreachable:', gc.collect()) # note that the cyclic reference doesn't matter
print('uncollectable:', gc.collect())
l2 = wr()
print('Collectable:', gc.collect())
l = l2
print(gc.garbage)
del l, l2
print('unreachable:', gc.collect())
print('uncollectable:', gc.collect())
print('Collectable:', gc.collect())
print(gc.garbage)
import gc
gc.set_debug(gc.DEBUG_STATS)
#with gc.get_stats() as stats:
#    for s in stats:
#        print(s)
#print(gc.get_stats())
#gc.disable
