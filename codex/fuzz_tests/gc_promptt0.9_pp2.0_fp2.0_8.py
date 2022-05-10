import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect():
def f():
    o1 = C()
    o2 = C()
    o3 = o1
    o2.next = o1
    o1.next = o2
    o3.next = None
    gc.collect()
del f
gc.collect()
print("collectable", gc.collect())
gc.garbage[0].count = 42
gc.garbage[0].count
gc.collect()

 
# Ref-counting is off by default:
del gc.garbage[0].next
gc.collect()                                # Dangling cycles not found
print("garbage", gc.garbage)
gc.collect()                                # cleared on second pass
print("garbage", gc.garbage)


# Ref counting plus cyclic gc:
gc.set_debug(gc.DEBUG_SAVEALL)
def f():
    o1 = C()
    o2 = C()
    o3 = o1
    o2.next = o1
    o1.next = o2
    o3.next = None
f
