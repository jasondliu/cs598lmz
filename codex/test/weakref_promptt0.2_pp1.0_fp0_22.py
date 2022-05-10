import weakref
# Test weakref.ref(x) == weakref.ref(x)

class C:
    pass

c = C()

r1 = weakref.ref(c)
r2 = weakref.ref(c)

print(r1 == r2)

# Test weakref.ref(x) is weakref.ref(x)

print(r1 is r2)

# Test weakref.ref(x) == weakref.ref(y)

c2 = C()

r3 = weakref.ref(c2)

print(r1 == r3)

# Test weakref.ref(x) is weakref.ref(y)

print(r1 is r3)

# Test weakref.ref(x) == x

print(r1 == c)

# Test weakref.ref(x) is x

print(r1 is c)

# Test x == weakref.ref(x)

print(c == r1)

# Test x is weakref.ref(x)

print(c is r1)


