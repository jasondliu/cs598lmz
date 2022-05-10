import weakref
# Test weakref.ref(a)
class A:
    pass
a = A()
r = weakref.ref(a)
assert type(r) is weakref.ReferenceType
assert r() is a

# Test weakref.ref(a, cb)
def cb(r):
    cb.called = True
cb.called = False
r = weakref.ref(a, cb)
assert type(r) is weakref.ReferenceType
assert r() is a
assert cb.called == False
del a
assert cb.called == True

# Test weakref.ref(a, cb, ...)
