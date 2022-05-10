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

print(r() is o)
print(r2() is o2)

print(r() is o2)
print(r2() is o)

print(r() == o)
print(r2() == o2)

print(r() == o2)
print(r2() == o)

print(r() != o)
print(r2() != o2)

print(r() != o2)
print(r2() != o)

print(r == o)
print(r2 == o2)

print(r == o2)
print(r2 == o)

print(r != o)
print(r2 != o2)

