import weakref
# Test weakref.ref()

import weakref

class Foo(object):
    pass

foo = Foo()

def callback(ref):
    print "callback called:", ref()

r = weakref.ref(foo, callback)

print r() is foo
print r()

del foo

print r()

print '-'*60

a = Foo()
b = Foo()

r = weakref.ref(a, callback)

print r() is a
print r()

del a

print r()

print '-'*60

a = Foo()
b = Foo()

r = weakref.ref(a, callback)

print r() is a
print r()

del b

print r()

print '-'*60

a = Foo()
b = Foo()

r = weakref.ref(a, callback)

print r() is a
print r()

del a
del b

print r()

print '-'*60

a = Foo()
b = Foo()

r = weakref.ref(
