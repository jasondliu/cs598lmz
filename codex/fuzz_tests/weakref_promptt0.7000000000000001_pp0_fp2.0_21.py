import weakref
# Test weakref.ref for new style classes

class C(object):
    pass

c = C()
r = weakref.ref(c)
c.x = r

print 'c.x is c', c.x is c
print 'c.x is r', c.x is r

print 'r() is c', r() is c
print 'r() is r', r() is r

del c
assert r() is None
