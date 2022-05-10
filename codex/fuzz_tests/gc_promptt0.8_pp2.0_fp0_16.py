import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() without a collection pass
# a = []
# weakref.ref(a)
# gc.collect()
# Test gc.collect() with a collection pass
# a = []
# weakref.ref(a)
# gc.collect()
# Test gc.collect() after a collection pass
# a = []
# weakref.ref(a)
# gc.collect()
# Test gc.collect() after a collection pass
# a = []
# weakref.ref(a)
# gc.collect()


# assert gc.collect() == 0
# for i in range(10):
#     a = []
#     a.append(a)
#     b = a
#     del a
#     b.append(b)
#     c = b[0]
#     del b
#     assert gc.collect() == 0

# assert gc.collect() == 1
# assert gc.collect() == 0

# assert gc.collect() == 1
# assert gc.collect() == 1
# assert gc.collect()
