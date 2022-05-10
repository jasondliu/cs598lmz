import weakref
# Test weakref.ref()

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

del o2
print(r2())

o = C()
r = weakref.ref(o)
print(r)
print(r())

del o
print(r())

o = C()
r = weakref.ref(o)
print(r)
print(r())

o2 = r()
print(o2)
print(r())

del o
print(r())

del o2
print(r())

# Test weakref.proxy()

class C:
    pass

o = C()
p = weakref.proxy(o)
print(p)

o2 = C()
p2 = weakref.proxy(o2)
print(p2)

del o2
print(p2)

o = C()
