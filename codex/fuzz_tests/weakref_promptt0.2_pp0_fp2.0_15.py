import weakref
# Test weakref.ref()
import sys

class C:
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

print 'o:', o
print 'r:', r
print 'r():', r()

del o
print 'r():', r()

# Test weakref.proxy()
import weakref

class C:
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return 'C(%r)' % self.x

o = C(1)
p = weakref.proxy(o)

print 'o:', o
print 'p:', p
print 'p.x:', p.x

o
