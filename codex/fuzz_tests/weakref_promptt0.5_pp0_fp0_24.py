import weakref
# Test weakref.ref() and weakref.proxy() with a class instance.

class C(object):
    def __init__(self, n):
        self.n = n
    def __repr__(self):
        return 'C(%s)' % self.n

def f(x, y):
    print x, y

o = C(1)
r = weakref.ref(o)
print 'r =', r
print 'r() =', r()
print 'r() is o =', r() is o
print 'r() is C(1) =', r() is C(1)
print

p = weakref.proxy(o)
print 'p =', p
print 'p is o =', p is o
print 'p is C(1) =', p is C(1)
print

o2 = C(2)
print 'o2 =', o2
print 'o2 is C(2) =', o2 is C(2)
print

print 'r() =', r()
print 'p =', p
print

o = o2
