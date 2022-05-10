import weakref
# Test weakref.ref

class A:
    def __init__(self, x=0):
        self.x = x

a = A(1)
b = A(2)

r = weakref.ref(a)
s = weakref.ref(b)

assert r() is a
assert s() is b
assert r() is not None
assert s() is not None

del a
del b

#print(r())
#print(s())

assert r() is None
assert s() is None

a = A(1)
b = A(2)

r = weakref.ref(a)
s = weakref.ref(b)
t = weakref.ref(a)

assert r() is a
assert t() is a and r is t
assert r() is not b
assert s() is b
assert r() is not s()

del a

assert r() is None
assert s() is b
assert t() is None

del b

assert s() is None

# Test weakref.proxy

