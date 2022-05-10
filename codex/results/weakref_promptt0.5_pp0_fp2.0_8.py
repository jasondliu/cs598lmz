import weakref
# Test weakref.ref()
class Foo(object):
    pass

f = Foo()

# Create a weak reference to f
f_ref = weakref.ref(f)
print f_ref

print f_ref() is f

f = None
print f_ref()

print f_ref() is None

# Test weakref.WeakValueDictionary()
class Foo(object):
    pass

f = Foo()

d = weakref.WeakValueDictionary()
d['foo'] = f

print d['foo'] is f

f = None

try:
    print d['foo']
except KeyError:
    print 'KeyError'

# Test weakref.WeakKeyDictionary()
class Foo(object):
    pass

f = Foo()

d = weakref.WeakKeyDictionary()
d[f] = 1

print d[f] == 1

f = None

try:
    print d[f]
except KeyError:
    print 'KeyError'
