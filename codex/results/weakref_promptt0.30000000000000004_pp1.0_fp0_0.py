import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())
print(r() is o)

o2 = C()
r2 = weakref.ref(o2)
print(r2)
print(r2())
print(r2() is o2)

print(r is r2)
print(r() is r2())

o = None
print(r())

r = None
print(r2())

o2 = None
print(r2())

r2 = None

# Test weakref.proxy()

class C:
    pass

o = C()
p = weakref.proxy(o)
print(p)
print(p is o)
print(type(p))

o2 = C()
p2 = weakref.proxy(o2)
print(p2)
print(p2 is o2)
print(type(p2))

print(p is p2)
print(p is o2)
print(
