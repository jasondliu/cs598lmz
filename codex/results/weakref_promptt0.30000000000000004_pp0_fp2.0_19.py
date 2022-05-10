import weakref
# Test weakref.ref(x) == weakref.ref(x)

class C:
    pass

c = C()

r1 = weakref.ref(c)
r2 = weakref.ref(c)

print(r1 == r2)

del c

print(r1 == r2)

# Test weakref.ref(x) is weakref.ref(x)

class C:
    pass

c = C()

r1 = weakref.ref(c)
r2 = weakref.ref(c)

print(r1 is r2)

del c

print(r1 is r2)

# Test weakref.ref(x) == weakref.ref(y)

class C:
    pass

c1 = C()
c2 = C()

r1 = weakref.ref(c1)
r2 = weakref.ref(c2)

print(r1 == r2)

del c1, c2

print(r1 == r2)

# Test weakref.ref(x
