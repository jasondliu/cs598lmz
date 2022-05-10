import weakref
# Test weakref.ref()

class Foo(object):
    pass

f = Foo()
r = weakref.ref(f)
print r
print r()
print f is r()

del f
print r()

# Test weakref.WeakValueDictionary()

class Foo(object):
    pass

f = Foo()
d = weakref.WeakValueDictionary()
d['foo'] = f
print d['foo']
print f is d['foo']

del f
try: print d['foo']
except KeyError: print 'KeyError'

# Test weakref.WeakKeyDictionary()

class Foo(object):
    pass

f = Foo()
d = weakref.WeakKeyDictionary()
d[f] = 'foo'
print d[f]
print d[f] is d[f]

del f
try: print d[f]
except KeyError: print 'KeyError'

# Test weakref.WeakSet()

class Foo(object):
    pass

f = Foo()
s = weakref.WeakSet([f])

