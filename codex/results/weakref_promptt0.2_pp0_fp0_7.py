import weakref
# Test weakref.ref()

class C(object):
    pass

o = C()
r = weakref.ref(o)
print r() is o

del o
print r() is None

o = C()
r = weakref.ref(o)
print r() is o

o2 = o
r2 = r
del o, r
print r2() is o2

del o2
print r2() is None

# Test weakref.proxy()

class C(object):
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return 'C(%r)' % self.x

o = C(42)
p = weakref.proxy(o)
print p.x
print p

del o
try:
    print p.x
except ReferenceError:
    print 'ReferenceError'

o = C(42)
p = weakref.proxy(o)
print p.x
print p

o2 = o
p2 = p
del o, p
print p2
