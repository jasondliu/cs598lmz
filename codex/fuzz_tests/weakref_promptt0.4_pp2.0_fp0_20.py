import weakref
# Test weakref.ref(a) == weakref.ref(a)
#
# This test is not in the test_weakref module because it relies on
# weakref.ref being a class, which is not the case in Python 2.

class C:
    pass

a = C()
b = C()

assert weakref.ref(a) == weakref.ref(a)
assert weakref.ref(b) == weakref.ref(b)
assert not (weakref.ref(a) == weakref.ref(b))
assert not (weakref.ref(b) == weakref.ref(a))
assert not (weakref.ref(a) == b)
assert not (weakref.ref(b) == a)
assert not (a == weakref.ref(b))
assert not (b == weakref.ref(a))

assert not (weakref.ref(a) != weakref.ref(a))
assert not (weakref.ref(b) != weakref.ref(b))
assert weakref.ref(a) != weakref.ref(b)
assert weakref
