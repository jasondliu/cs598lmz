import weakref
# Test weakref.ref()
r = weakref.ref(t)
r()

r() is None

import sys
sys.getrefcount(t)

r = weakref.ref(t)
sys.getrefcount(t)

sys.getrefcount(t) == 1

del t

try:
    print r()
except:
    print "pass"

# Test weakref.proxy()
class C(object):
    def __init__(self, n):
        self.n = n
        
a = C(42)
class D(object):
    def __init__(self):
        self.a = a

d = D()
p = weakref.proxy(d)

assert p.a.n == 42
del d

try:
    print p.a
except:
    print "pass"

a = C(42)
p1 = weakref.proxy(a)
p2 = weakref.proxy(a)

try:
    p1 is p2
except:
    print "pass"

# Test weakref
