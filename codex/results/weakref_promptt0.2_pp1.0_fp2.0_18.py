import weakref
# Test weakref.ref(obj)

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())

o2 = C()
r2 = weakref.ref(o2)
print(r2)
print(r2())

o = o2 = None
print(r())
print(r2())

# Test weakref.ref(obj, callback)

L = []

class C:
    pass

o = C()
r = weakref.ref(o, L.append)
print(r)
print(r())

o2 = C()
r2 = weakref.ref(o2, L.append)
print(r2)
print(r2())

o = o2 = None
print(r())
print(r2())
print(L)

# Test weakref.proxy(obj[, callback])

L = []

class C:
    pass

o = C()
p = weakref.proxy(o, L.append)
print(p)

