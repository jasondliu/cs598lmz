import weakref
# Test weakref.ref()

class A(object):
    pass

a = A()
a.x = A()
a.x.y = A()
a.x.y.z = a

x = weakref.ref(a)
print x() is a
print x().x.y.z is a
print x().x.y.z.x.y.z is a

a = None
print x() is None

# Test weakref.proxy()

a = A()
a.x = A()
a.x.y = A()
a.x.y.z = a

x = weakref.proxy(a)
print x is a
print x.x.y.z is a
print x.x.y.z.x.y.z is a

a = None
try:
    print x.x
except ReferenceError:
    pass
else:
    print "expected exception"

# Test weakref.getweakrefcount() and getweakrefs()

a = A()
a.x = A()
a.x.y = A
