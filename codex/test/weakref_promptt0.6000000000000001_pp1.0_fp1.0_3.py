import weakref
# Test weakref.ref(A)
class A: pass
a = A()
r = weakref.ref(a)
assert r() is a
assert r is weakref.ref(a)

# Test weakref.ref(A, callback)
class A: pass
a = A()
r = weakref.ref(a, lambda w: None)
assert r() is a
assert r is weakref.ref(a)

# Test weakref.ref(A, callback) with a callback that raises
class A: pass
a = A()
def callback(w):
    raise Exception
r = weakref.ref(a, callback)
assert r() is a
assert r is weakref.ref(a)

# Test weakref.ref(A, callback) with a callback that raises
# with an implicit error message
class A: pass
a = A()
def callback(w):
    raise TypeError
r = weakref.ref(a, callback)
assert r() is a
assert r is weakref.ref(a)

# Test weakref.proxy(A)
class A: pass
a
