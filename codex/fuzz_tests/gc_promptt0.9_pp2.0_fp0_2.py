import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
s = set([])
a = set([])
b = set([])
c = set([])
print gc.collect()
print sys.gettotalrefcount()
print sys.getrefcount(a)
w = weakref.proxy(a)
print sys.getrefcount(a)
print sys.getrefcount(b)
print sys.getrefcount(c)
del a
print gc.collect()
print sys.getrefcount(b)
print sys.getrefcount(c)
