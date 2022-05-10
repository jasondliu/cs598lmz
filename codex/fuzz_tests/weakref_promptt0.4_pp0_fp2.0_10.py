import weakref
# Test weakref.ref

class C(object):
    pass

o = C()
r = weakref.ref(o)

print r() is o

del o
print r() is None

try:
    print r()
except ReferenceError:
    pass
else:
    print 'Expected ReferenceError'

class D(object):
    def __init__(self, x):
        self.x = x

o = D(42)
r = weakref.ref(o)
print r().x

del o
try:
    print r().x
except ReferenceError:
    pass
else:
    print 'Expected ReferenceError'

# Test weakref.proxy

o = C()
p = weakref.proxy(o)

print p is o

del o
try:
    print p
except ReferenceError:
    pass
else:
    print 'Expected ReferenceError'

o = D(42)
p = weakref.proxy(o)
print p.x

del o
try:
    print p.x
except ReferenceError:
