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

l = [o, o2]
print 'l:', l

del o, o2
gc.collect()

print 'r():', r()
print 'r2():', r2()

# Test weakref.proxy()

class C:
    def __init__(self, x=42):
        self.x = x

    def spam(self, y):
        print 'C.spam:', self, y

o = C()
p = weakref.proxy(o)

print 'o:', o
print 'p:', p
print
