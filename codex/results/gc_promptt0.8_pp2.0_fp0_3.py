import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

print("===========================gc.collect()=================================")
a = weakref.ref(object())
print("{0}:{1}".format(hex(id(a)), hex(id(a()))))

gc.collect()
print("{0}:{1}".format(hex(id(a)), hex(id(a()))))

a = None
gc.collect()
print("{0}:{1}".format(hex(id(a)), hex(id(a()))))

print("=================================gc.DEBUG_COLLECTABLE=================================")
a = None
gc.collect()
gc.set_debug(gc.DEBUG_COLLECTABLE)

gc.collect()

print(gc.garbage)

# Test gc.DEBUG_SAVEALL
print("=================================gc.DEBUG_SAVEALL=================================")
gc.set_debug(gc.DEBUG_SAVEALL)

gc.collect()

print(gc.garbage)

# Test gc.DEBUG_UNCOLLECTABLE
print("=================================gc.DEBUG_UNCOLLECTABLE================================
