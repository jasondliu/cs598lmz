import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() cycles
import sys
def f(x):
    print sys.getrefcount(x)-2
    x.append(x)

gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
gc.collect()
l = []
# f(l)
# f(l)
# f(l)
# f(l)
# f(l)
# del l
# gc.collect()

# Test collect empty containers:
gc.set_debug(gc.DEBUG_COLLECTABLE)
gc.collect()
print gc.collect()

# Test collect builtin module namespace
gc.collect()
import sys
gc.collect()

# Test collector_info()
def show_collection_stats():
    print "Collections:", gc.get_count()
    print "Collected:", gc.collect()

show_collection_stats()
gc.set_debug(gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE)
lst = []
show_collection_stats()

class A:
    pass
a =
