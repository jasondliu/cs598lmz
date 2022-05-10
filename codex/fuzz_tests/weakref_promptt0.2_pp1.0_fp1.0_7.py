import weakref
# Test weakref.ref()
import gc
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

print 'gc.collect():'
n = gc.collect()
print 'gc.collect() returned', n

print 'r2():', r2()

# Test weakref.proxy()

o = C()
p = weakref.proxy(o)

print 'o:', o
print 'p:', p
print 'p.x = 1:'
p.x = 1
print 'o.x =', o.x
print 'p.x =', p.x

del o
print 'p.x =', p.x

# Test weakref.
