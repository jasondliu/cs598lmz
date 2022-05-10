import weakref
# Test weakref.ref(object, callback)

import weakref
import gc

class A(object):
    pass

a = A()
r = weakref.ref(a, lambda x: x is None)
assert r() is a

del a
gc.collect()
assert r() is None

# Test weakref.ref(object)

import weakref

class A(object):
    pass

a = A()
r = weakref.ref(a)
assert r() is a

del a
assert r() is None

# Test weakref.proxy(object, callback)

import weakref
import gc

class A(object):
    pass

a = A()
r = weakref.proxy(a, lambda x: x is None)
assert r is a

del a
gc.collect()
try:
    r is None
except ReferenceError:
    pass
else:
    assert False, 'expected ReferenceError'

# Test weakref.proxy(object)

import weakref

class A(object):
    pass

a = A
