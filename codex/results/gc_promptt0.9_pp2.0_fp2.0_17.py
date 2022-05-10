import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
print "Raw Copy Mem Usage:", memory_usage
r = [weakref.ref(i) for i in range(1000)]
print "Ref Mem Usage:", memory_usage

def ref(i):
    return i

for i in range(1000):
    x = [0]*10*i
    ref(x)
print "Copy Mem Usage:", memory_usage
gc.collect()
print "Ref gc Mem Usage:", memory_usage
import gc
gc.collect()
from sys import version_info
if version_info[0] > 2:
    print("WARNING: Please use Python 2 instead of Python 3")
