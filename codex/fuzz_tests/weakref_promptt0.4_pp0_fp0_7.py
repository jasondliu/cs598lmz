import weakref
# Test weakref.ref() and weakref.proxy()

# Create a list of objects to keep them alive
objects = []

class C(object):
    pass

def f():
    o = C()
    objects.append(o)
    return o

o = f()
r = weakref.ref(o)
p = weakref.proxy(o)

print o, r(), p

del o
print r(), p

o = f()
print o, r(), p

del o
print r(), p

o = f()
print o, r(), p

del o
print r(), p

o = f()
print o, r(), p

del o
print r(), p

o = f()
print o, r(), p

del o
print r(), p

o = f()
print o, r(), p

del o
print r(), p

o = f()
print o, r(), p

del o
print r(), p

o = f()
print o, r(), p

del o
print r(), p


