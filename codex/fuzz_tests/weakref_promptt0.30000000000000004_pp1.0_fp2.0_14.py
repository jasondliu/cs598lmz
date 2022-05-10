import weakref
# Test weakref.ref(x) == weakref.ref(x)

class C(object):
    pass

c = C()

r = weakref.ref(c)

assert r == r
assert r == weakref.ref(c)
assert weakref.ref(c) == r
assert weakref.ref(c) == weakref.ref(c)

assert not (r != r)
assert not (r != weakref.ref(c))
assert not (weakref.ref(c) != r)
assert not (weakref.ref(c) != weakref.ref(c))

assert r is r
assert r is weakref.ref(c)
assert weakref.ref(c) is r
assert weakref.ref(c) is weakref.ref(c)

assert not (r is not r)
assert not (r is not weakref.ref(c))
assert not (weakref.ref(c) is not r)
assert not (weakref.ref(c) is not weakref.ref(c))

assert r == c
assert c == r
assert
