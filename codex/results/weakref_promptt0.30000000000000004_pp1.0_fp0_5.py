import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)

print(r)
print(r())

o2 = r()
print(o is o2)

o3 = C()
r2 = weakref.ref(o3)
print(r2)
print(r2())

o4 = r2()
print(o3 is o4)

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

print(r is None)
print(r() is None)
