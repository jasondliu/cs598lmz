import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# 1. Call gc.collect() and call gc.garbage to verfiy
# ----- normal case
#
gc.collect()
print(gc.garbage)
## []
#
# ----- with many objects, 1 cyclic
#
# gc.garbage has all unreachable objects in it (just like in CPython)

class A:
    def __del__(self):
        print('Deleting A')
class B:
    def __del__(self):
        print('Deleting B')
a = A()
b = B()
L1 = [a, b]
L2 = [a, b]
a.x = L1
b.x = L2
x = [a, b]
gc.collect()
print(gc.garbage)
## [{'x': [{...}, {...}]}]
#
# 2. Call gc.collect() and call gc.garbage to verfiy
# Now break the cycle
del a.x
gc.collect()
print(gc.garbage)
##
