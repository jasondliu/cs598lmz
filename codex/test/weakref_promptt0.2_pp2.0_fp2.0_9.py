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

print(r is None)
print(r() is None)

print(None is r)
print(None is r())

print(r == None)
print(r() == None)

print(None == r)
print(None == r())

# Test weakref.proxy()

o = C()
p = weakref.proxy(o)
print(p)

o2 = C()
p2 = weakref.proxy(o2)
print(p2)

