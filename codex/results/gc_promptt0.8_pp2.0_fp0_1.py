import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable()
gc.collectable(weakref.ref(o)) # Check that weakrefs are collectable.
gc.collectable(1) # Integers are not collectable.
gc.collectable(o) # Objects do not have __del__ methods.
gc.collectable(o2)
gc.collectable(o3)
gc.collectable(o4)
print()

# Test gc.get_debug() and gc.set_debug()
print(gc.get_debug(), gc.DEBUG_LEAK, gc.DEBUG_STATS, gc.DEBUG_COLLECTABLE)
print()

# Test gc.garbage:
print(gc.garbage)
print()
# Not very useful, but here's how to force it to grow:
for i in range(3):
    try:
        del gc.garbage[0]
    except IndexError:
        break
    else:
        gc.garbage.append(gc.garbage)
print(gc.garbage)

# The following code demonstrates that objects are only collected
#
