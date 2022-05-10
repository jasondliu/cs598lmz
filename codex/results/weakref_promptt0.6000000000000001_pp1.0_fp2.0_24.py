import weakref
# Test weakref.ref()

import weakref
import gc

class A:
    pass
a = A()
r = weakref.ref(a)
print(r)
print(r())
print(gc.get_referents(a))

del a
print(gc.collect())
print(gc.get_referrers(r))
print(r)
print(r())

# Test weakref.ref(None)

import weakref

r = weakref.ref(None)
print(r)
print(r())

# Test weakref.ref(object())

import weakref

r = weakref.ref(object())
print(r)
print(r())

# Test weakref.WeakValueDictionary()

import weakref

d = weakref.WeakValueDictionary()
print(d)

# Test weakref.WeakValueDictionary({})

import weakref

d = weakref.WeakValueDictionary({})
print(d)

# Test weakref.WeakValueDictionary({1:1})

import weakref
