import weakref
# Test weakref.ref(object)

# Test the basic operations

class Object:
    pass

o = Object()
r = weakref.ref(o)
assert r() is o
assert r() is o
assert r() is o

# Test equality

class Object:
    pass

o1 = Object()
o2 = Object()

r1 = weakref.ref(o1)
r2 = weakref.ref(o2)
assert r1 == r1
assert r1 != r2
assert not r1 != r1
assert not r1 == r2

# Test repr

class Object:
    pass

o = Object()
r = weakref.ref(o)
repr(r)

# Test hash

class Object:
    pass

o1 = Object()
o2 = Object()

r1 = weakref.ref(o1)
r2 = weakref.ref(o2)
assert hash(r1) == hash(r1)
assert hash(r1) != hash(r2)
assert hash(r1) != hash(
