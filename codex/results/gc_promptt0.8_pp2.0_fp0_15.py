import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
# gc.collect()
# gc.collect()
# del l
# gc.collect()
# gc.collect()
# gc.collect()
# gc.collect()
# gc.collect()


# class C(object):
#     def __del__(self):
#         print 'C.__del__'
# 
# for i in xrange(10000):
#     C()
# 
# gc.collect()
# print gc.collect()
# print gc.collect()

# print gc.get_threshold()

# 
# # non heapsize
# f = [None] * 10
# f[0] = f
# del f
# f = None
# gc.collect()
# gc.collect()
# gc.collect()
# # heapsize
# f = [None] * 10
# gc.collect()
# gc.collect()
# gc.collect()
# gc.collect()
# gc.collect()
# gc.collect()

