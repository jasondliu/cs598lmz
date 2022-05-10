import weakref
# Test weakref.ref() and weakref.proxy()

import weakref

class C(object):
    pass

o = C()
r = weakref.ref(o)
p = weakref.proxy(o)

print 'o:', o
print 'r:', r
print 'p:', p
print 'r():', r()
print 'p.attr:', p.attr

o.attr = 1
print 'o.attr:', o.attr
print 'r().attr:', r().attr
print 'p.attr:', p.attr

del o
print 'o:', o
print 'r():', r()
print 'p.attr:', p.attr
