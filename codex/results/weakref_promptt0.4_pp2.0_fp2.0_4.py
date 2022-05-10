import weakref
# Test weakref.ref(a) == weakref.ref(a)

class C(object):
    pass

a = C()
b = C()

# Test equality of two refs to the same object
assert weakref.ref(a) == weakref.ref(a)

# Test equality of two refs to different objects
assert weakref.ref(a) != weakref.ref(b)

# Test equality of a ref to an object and the object itself
assert weakref.ref(a) == a

# Test equality of a ref to an object and the object itself
assert a == weakref.ref(a)

# Test equality of a ref to an object and the object itself
assert weakref.ref(a) != b

# Test equality of a ref to an object and the object itself
assert b != weakref.ref(a)

# Test equality of a ref to an object and a proxy to the object
assert weakref.ref(a) == weakref.proxy(a)

# Test equality of a ref to an object and a proxy to the object
assert weakref.proxy(a)
