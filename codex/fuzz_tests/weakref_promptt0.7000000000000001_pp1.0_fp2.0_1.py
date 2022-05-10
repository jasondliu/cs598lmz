import weakref
# Test weakref.ref and weakref.WeakValueDictionary.

class Foo(object):
    pass

def callback(r):
    print r

foo = Foo()

a = weakref.ref(foo, callback)

b = weakref.WeakValueDictionary()
b[1] = foo

del foo
del a
del b
