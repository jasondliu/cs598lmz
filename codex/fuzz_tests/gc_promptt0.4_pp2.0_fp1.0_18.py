import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback.

class A:
    pass

class B:
    pass

class C:
    pass

def callback(wr):
    print "callback", wr()

def callback2(wr):
    print "callback2", wr()

a = A()
b = B()
c = C()

a.b = b
b.a = a

# A cycle, with a callback for a
a.wr = weakref.ref(a, callback)

# A cycle, with a callback for b
b.wr = weakref.ref(b, callback2)

# A cycle, no callback
c.wr = weakref.ref(c)

# No cycle, no callback
d = A()

# No cycle, with a callback
e = A()
e.wr = weakref.ref(e, callback)

# No cycle, with a callback
f = A()
f.wr = weakref.ref(f, callback2)

print gc.collect()
print gc.collect()
print gc.collect()
