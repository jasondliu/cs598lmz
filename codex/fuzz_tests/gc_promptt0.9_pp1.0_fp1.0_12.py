import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect().
w = weakref.ref(Noisy())
del x
ref = weakref.ref(y)
del y
check_class_counters(Noisy, collected=[1])
for st, et in gc.DEBUG_SAVEALL:
    gc.collect()
    check_class_counters(Noisy, collected=[1], uncollectable=[1])
    gc.collect(0)
    check_class_counters(Noisy, collected=[1])
    # for some reason this test fails if it is done here
    # instead of other place

 
# Test weakref finalizing:

del z
check_class_counters(Noisy, finalizing=[2])
check_class_counters(Noisy, finalizing=[2])
gc.collect()
check_class_counters(Noisy, finalizing=[2])
gc.collect(0)
check_class_counters(Noisy, finalizing=[2])
#w = weakref.ref(Noisy())
#try:
#    check_class_counters(Noisy, finalizing=[
