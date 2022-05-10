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

print(r is r2)
print(r() is r2())

print(r == r2)
print(r() == r2())

print(r is r)
print(r() is r())

print(r == r)
print(r() == r())

print(r is not r2)
print(r() is not r2())

print(r != r2)
print(r() != r2())

print(r is not r)
print(r() is not r())

print(r != r)
print(r() != r())

# Test weakref.proxy()

o = C()
p = weakref.proxy(o)
print(p)

o2 = C()
p2 = weakref.proxy(o2)
