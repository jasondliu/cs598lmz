import weakref
# Test weakref.ref() and weakref.proxy()

class C:
    pass

o = C()
r = weakref.ref(o)
p = weakref.proxy(o)

print(r)
print(p)

print(r())
print(p)

del o
print(r())
print(p)

o2 = C()
r2 = weakref.ref(o2)
p2 = weakref.proxy(o2)
print(r2)
print(p2)

print(r2())
print(p2)

print(r == r2)
print(p == p2)

print(r is r2)
print(p is p2)

print(r() == r2())
print(p == p2)

print(r() is r2())
print(p is p2)

print(r() == o2)
print(p == o2)

print(r() is o2)
print(p is o2)

print(r == o2)
print(p == o2
