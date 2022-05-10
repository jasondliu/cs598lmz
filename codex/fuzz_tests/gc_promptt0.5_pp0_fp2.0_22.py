import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass

a = A()
b = A()
b.a = a
a.b = b
del a, b
gc.collect()

# Test gc.garbage
class C:
    pass

a = C()
b = C()
a.b = b
b.a = a
del a, b
gc.collect()
print gc.garbage

# Test weakrefs
class A:
    pass

a = A()
b = A()
b.a = a
a.b = b
w = weakref.ref(a)
del a, b
print w()
gc.collect()
print w()

# Test finalizers
class A:
    pass

a = A()
b = A()
b.a = a
a.b = b
def callback(wr):
    print "callback called"

w = weakref.ref(a, callback)
del a, b
print w()
gc.collect()
print w()

# Test weakrefs with finalizers
class A
