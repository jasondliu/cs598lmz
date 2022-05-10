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

print(r is o)
print(r() is o)

print(r == o)
print(r() == o)

print(r is o2)
print(r() is o2)

print(r == o2)
print(r() == o2)

print(r is None)
print(r() is None)

print(r == None)
print(r() == None)

print(None is r)
print(None is r())

print(None == r)
print(None == r())

print(r is not None)
print(r() is not None)

print(r
