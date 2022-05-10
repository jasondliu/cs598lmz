import weakref
# Test weakref.ref(a) == weakref.ref(a)

class A:
    pass

a = A()
b = A()

r1 = weakref.ref(a)
r2 = weakref.ref(a)
r3 = weakref.ref(b)
r4 = weakref.ref(b)

print(r1 == r2)
print(r2 == r3)
