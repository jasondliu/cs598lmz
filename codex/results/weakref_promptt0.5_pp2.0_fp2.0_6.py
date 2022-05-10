import weakref
# Test weakref.ref()
import gc
import pickle

class C(object):
    pass

o = C()
r = weakref.ref(o)

print r(), r() is o

o2 = C()
r2 = weakref.ref(o2)

print r2(), r2() is o2

o = o2 = None

gc.collect()

print r(), r() is None
print r2(), r2() is None

# Test weakref.proxy()

print 'Test weakref.proxy()'

class C(object):
    pass

o = C()
p = weakref.proxy(o)

print p, p is o

o.foo = 12
print p.foo

o = C()
p = weakref.proxy(o)

print p, p is o

o.foo = 12
print p.foo

o = o2 = None

gc.collect()

try:
    print p.foo
except ReferenceError:
    print 'ReferenceError'

try:
    print p

