import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#gc.collect()
#print(gc.garbage)
#s = "123"
#del s
#print(gc.garbage)
#gc.collect()
#print(gc.garbage)

# Test weak reference
#a = "123"
#b = "456"
#c = weakref.ref(a)
#d = weakref.ref(b)
#print(c())
#print(d())
#del a
#print(c())
#print(d())
#del b
#print(c())
#print(d())
#gc.collect()
#print(c())
#print(d())

# Test
#a = "123"
#b = "456"
#c = weakref.ref(a)
#d = weakref.ref(b)
#print(c())
#print(d())
#del a
#b = None
#gc.collect()
#print(c())
#print(d())

# Test
a = "123"
b = "456"
c = weakref
