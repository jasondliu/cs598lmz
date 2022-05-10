import weakref
# Test weakref.ref() using same data:
a = [1, 2, 3]
b = a
print b

d = weakref.ref(a)
print d
print d() is a

# Test weakref.proxy() using same data:
r = weakref.proxy(a)
print r
print r is a

# Test weakref.ref() with new data:
e = weakref.ref(['string'])
print e()
print e()[0]
print e() is a
print e() is ['string'] # nope

# Test weakref.proxy() with new data:
s = weakref.proxy(['string'])
print s
print s is a
print s is ['string']

# But proxy can instantiate from a weakref:
p = weakref.proxy(a)
print p

# Test weakref.proxy() for attribute access:
try:
    print s.bar
except ReferenceError:
    print '*** Proxy without attribute'

class Foo(object):
    bar = 'baz'

f = Foo()
f_proxy = weak
