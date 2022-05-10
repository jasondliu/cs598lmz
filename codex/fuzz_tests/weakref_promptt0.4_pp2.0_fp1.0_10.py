import weakref
# Test weakref.ref

import weakref
import gc

class C(object):
    pass

o = C()
r = weakref.ref(o)

print 'o:', o
print 'r:', r
print 'r():', r()

o2 = C()
r2 = weakref.ref(o2)

print 'o2:', o2
print 'r2:', r2
print 'r2():', r2()

del o2
print 'r2():', r2()

gc.collect()
print 'r2():', r2()

# Test weakref.proxy

import weakref

class C(object):
    def method(self):
        return id(self)

o = C()
p = weakref.proxy(o)

print 'o:', o
print 'p:', p
print 'p.method():', p.method()

o2 = C()
p2 = weakref.proxy(o2)

print 'o2:', o2
print 'p2:', p2
print '
