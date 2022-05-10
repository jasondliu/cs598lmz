import weakref
# Test weakref.ref

class C(object):
    pass

c = C()
r = weakref.ref(c)
print r

print r() is c
print r() is None

del c

print r() is None

class D(object):
    pass

d = D()
r = weakref.ref(d)
print r

print r() is d
print r() is None

del d

print r() is None

class E(object):
    pass

e = E()
r = weakref.ref(e)
print r

print r() is e
print r() is None

del e

print r() is None

class F(object):
    pass

f = F()
r = weakref.ref(f)
print r

print r() is f
print r() is None

del f

print r() is None

class G(object):
    pass

g = G()
r = weakref.ref(g)
print r

print r() is g
print r() is None

