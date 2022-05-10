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

print(r == r2)
print(r() == r2())

print(r is not r2)
print(r() is not r2())

print(r != r2)
print(r() != r2())

print(r < r2)
print(r() < r2())

print(r <= r2)
print(r() <= r2())

print(r > r2)
print(r() > r2())

print(r >= r2)
print(r() >= r2())

print(r + r2)
print(r() + r2())

