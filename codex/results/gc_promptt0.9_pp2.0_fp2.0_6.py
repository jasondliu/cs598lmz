import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass
a = A()
w = weakref.ref(a)
gc.collect()
# Test gc.collect() when mmust move objects to old generation
print("Adding large amounts of data to cause object movement")
print("\t(decrement a in loop to avoid optimizing away)")
a = [None] * 200
for i in range(500):
    a.append([])
    a[-1].append(a)
    del a[0]
    a = a[-1]
    a[0] = None
    a -= 1
del a, i
print("Collecting...")
gc.collect()
print("Done")
# Test weakref callback with objects that move to old generation
# (some of the code here is copied from above test)
print("Testing weak reference callbacks with objects that move")
print("\t(decrement a in loop to avoid optimizing away)")
# Register callback
callback = []
def mycallback(obj):
    callback.append(obj)
callback.append(None)
a = [None] *
