import weakref
# Test weakref.ref(a) is weakref.ref(a)

class A:
    pass

a = A()

r1 = weakref.ref(a)
r2 = weakref.ref(a)

print(r1 is r2)
