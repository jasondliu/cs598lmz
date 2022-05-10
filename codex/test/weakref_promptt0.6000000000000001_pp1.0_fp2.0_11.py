import weakref
# Test weakref.ref()

class C:
    pass

c = C()
r = weakref.ref(c)
assert r() is c

# Test weakref.getweakrefcount()

assert weakref.getweakrefcount(c) == 1

# Test weakref.getweakrefs()

assert weakref.getweakrefs(c) == [r]

# Test weakref.proxy()

p = weakref.proxy(c)

assert p is c
assert p.__class__ is C

# Test weakref.finalize()

x = []
def callback(wr, x=x):
    x.append(wr)

wr = weakref.finalize(c, callback)

assert wr.alive
assert not x

del c

import gc; gc.collect()
assert not wr.alive
assert x == [wr]

# Test weakref.WeakKeyDictionary

d = weakref.WeakKeyDictionary()

d[C()] = 1
d[C()] = 2

