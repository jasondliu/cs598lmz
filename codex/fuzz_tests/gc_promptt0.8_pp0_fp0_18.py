import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.get_objects()

x = []
x.append(x)
print(gc.collect())
print(len(gc.get_objects()))

x = []
x.append(x)
del x
print(gc.collect())
print(len(gc.get_objects()))

x = []
y = [x]
del x
print(gc.collect())
print(len(gc.get_objects()))

y = []
y.append(y)
del y
print(gc.collect())
print(len(gc.get_objects()))
# test gc.DEBUG_SAVEALL

gc.set_debug(gc.DEBUG_UNCOLLECTABLE|gc.DEBUG_SAVEALL)
x = []
x.append(x)
print(len(gc.garbage))
x = "abcd"
print(len(gc.garbage))
del x
print(len(gc.garbage))
print(gc.garbage)
print(gc.collect())
print(len(gc.garbage))
print
