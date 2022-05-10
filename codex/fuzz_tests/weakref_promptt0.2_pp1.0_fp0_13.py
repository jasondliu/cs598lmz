import weakref
# Test weakref.ref()

class Foo:
    pass

foo = Foo()
foo_ref = weakref.ref(foo)
print(foo_ref)
print(foo_ref())

foo = None
print(foo_ref)
print(foo_ref())

# Test weakref.WeakKeyDictionary()

class Foo:
    pass

foo1 = Foo()
foo2 = Foo()

d = weakref.WeakKeyDictionary()
d[foo1] = 'foo1'
d[foo2] = 'foo2'

print(d.data)

foo1 = None
print(d.data)

foo2 = None
print(d.data)

# Test weakref.WeakValueDictionary()

class Foo:
    pass

foo1 = Foo()
foo2 = Foo()

d = weakref.WeakValueDictionary()
d['foo1'] = foo1
d['foo2'] = foo2

print(d.data)

foo1 = None
print(d.data)

foo2 = None
print(d
