import weakref
# Test weakref.ref()

class A(object):
    pass

a = A()
a.x = A()
a.x.y = A()

wr = weakref.ref(a.x.y)
assert wr() is a.x.y
del a.x.y
assert wr() is None

# Test weakref.proxy()

class A(object):
    pass

a = A()
a.x = A()
a.x.y = A()

wr = weakref.proxy(a.x.y)
assert wr is a.x.y
del a.x.y
try:
    wr.foo
except ReferenceError:
    pass
else:
    assert False, 'expected ReferenceError'

# Test weakref.getweakrefcount()

class A(object):
    pass

a = A()
a.x = A()
a.x.y = A()

wr = weakref.ref(a.x.y)
assert weakref.getweakrefcount(a.x.y) == 1
assert weakref.get
