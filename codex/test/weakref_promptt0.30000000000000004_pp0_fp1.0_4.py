import weakref
# Test weakref.ref(x) == weakref.ref(x)

class C:
    pass

c = C()
assert weakref.ref(c) == weakref.ref(c)
assert weakref.ref(c) is weakref.ref(c)

# Test weakref.ref(x) == weakref.ref(y)

c1 = C()
c2 = C()
assert weakref.ref(c1) != weakref.ref(c2)
assert weakref.ref(c1) is not weakref.ref(c2)

# Test weakref.ref(x) == y

c = C()
assert weakref.ref(c) == c
assert weakref.ref(c) is c

# Test weakref.ref(x) == z

c = C()
assert weakref.ref(c) != 42

# Test x == weakref.ref(y)

c = C()
assert c == weakref.ref(c)
