import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A(object):
    pass

a = A()
b = A()
a.b = b
b.a = a

#a = None
#b = None

print gc.collect()

#print gc.collect()
#print gc.collect()

#print gc.collect()
#print gc.collect()

#print gc.collect()
#print gc.collect()

#print gc.collect()
#print gc.collect()

#print gc.collect()
#print gc.collect()

#print gc.collect()
#print gc.collect()

#print gc.collect()
#print gc.collect()

#print gc.collect()
#print gc.collect()

#print gc.collect()
#print gc.collect()

#print gc.collect()
#print gc.collect()

#print gc.collect()
#print gc.collect()

#print gc.collect()
#print gc.
