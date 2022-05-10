import weakref
# Test weakref.ref(x) == weakref.ref(x)

class A:
    pass

a = A()
r1 = weakref.ref(a)
r2 = weakref.ref(a)
print(r1 == r2)

a = None
print(r1 == r2)

a = A()
r2 = weakref.ref(a)
print(r1 == r2)

a = None
print(r1 == r2)

a = A()
r1 = weakref.ref(a)
print(r1 == r2)

a = None
print(r1 == r2)

a = A()
r2 = weakref.ref(a)
print(r1 == r2)

a = None
print(r1 == r2)

a = A()
r1 = weakref.ref(a)
print(r1 == r2)

a = None
print(r1 == r2)

a = A()
r2 = weakref.ref(a)
print(r1 == r2
