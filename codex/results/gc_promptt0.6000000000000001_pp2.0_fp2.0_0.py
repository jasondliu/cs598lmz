import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.garbage.

# Test 1:  verify that collect still returns 0 when there are no
# cycles to collect.

print '1'
gc.collect()
print '2'
print gc.collect()
print '3'
print gc.garbage
print '4'

# Test 2:  create a cycle and verify that collect returns the number
# of objects in the cycle.

print '5'
class C:
    pass

c1 = C()
c2 = C()
c1.c2 = c2
c2.c1 = c1

print gc.collect()
print '6'
print gc.garbage
print '7'

# Test 3:  verify that collect clears the garbage list.

print '8'
del c1, c2
print '9'
print gc.garbage
print '10'
print gc.collect()
print '11'
print gc.garbage
print '12'

# Test 4:  create a cycle and verify that collect clears the garbage
# list.
