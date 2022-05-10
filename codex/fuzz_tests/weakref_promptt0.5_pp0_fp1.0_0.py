import weakref
# Test weakref.ref
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
print 'gc.collect():', n

print 'r2():', r2()

o = C()
p = weakref.proxy(o)

print 'o:', o
print 'p:', p
print 'p.x = 1:'
p.x = 1
print 'o.x:', o.x

# Test weakref.proxy
import weakref

class C:
    def __init__(self):
        self.x = 1

o = C()
p = weakref
