import weakref
# Test weakref.ref().
class Foo(object):
    pass

f = Foo()
r = weakref.ref(f)

print isinstance(r, weakref.ReferenceType)
print r() is f
print r() is not f

f = None
print r() is None
print r() is not None

try:
    r()
except ReferenceError:
    print "ReferenceError"

# Test weakref.proxy().
class Foo(object):
    pass

f = Foo()
p = weakref.proxy(f)

print isinstance(p, weakref.ProxyType)
print p is f
print p is not f

f = None
try:
    p is None
except ReferenceError:
    print "ReferenceError"

try:
    p is not None
except ReferenceError:
    print "ReferenceError"

try:
    p
except ReferenceError:
    print "ReferenceError"

# Test weakref.getweakrefcount().
class Foo(object):
    pass

f = Foo()
r1 = weakref.ref(f)

