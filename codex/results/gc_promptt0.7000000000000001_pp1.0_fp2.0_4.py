import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
# Test gc.get_threshold()
gc.get_threshold()
gc.get_threshold() == (700, 10, 10)
# Test gc.set_threshold()
gc.set_threshold(200, 2, 2)
gc.get_threshold() == (200, 2, 2)
gc.set_threshold(700, 10, 10)
gc.get_threshold() == (700, 10, 10)
# Test refcounts
x = 'hello'
sys.getrefcount(x)
x = 'hello'
y = x
sys.getrefcount(x)
del y
sys.getrefcount(x)
# Test gc.get_count()
gc.get_count()
# Test gc.set_debug()
gc.set_debug(gc.DEBUG_LEAK)
gc.collect()
gc.set_debug(0)
# Test gc.get_objects()
gc.get_objects()
gc.collect()
gc.get_objects()
# Test gc.get
