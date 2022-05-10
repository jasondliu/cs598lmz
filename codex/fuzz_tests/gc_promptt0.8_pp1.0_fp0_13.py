import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

class A():
    pass

a = A()
b = A()
c = A()
d = A()
e = A()
f = A()
g = A()

refs = [weakref.ref(A) for i in xrange(5)]
print [x() for x in refs]
refs.append(weakref.ref(a))
refs.append(weakref.ref(b))
refs.append(weakref.ref(b))
refs.append(weakref.ref(c))
refs.append(weakref.ref(d))
refs.append(weakref.ref(d))
refs.append(weakref.ref(d))
refs.append(weakref.ref(e))
refs.append(weakref.ref(e))
refs.append(weakref.ref(e))
refs.append(weakref.ref(e))
refs.append(weakref.ref(f))
refs.append(weakref.ref(f))
refs.append
