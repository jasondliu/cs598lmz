import weakref
# Test weakref.ref()

class Foo(object):
    pass

foo = Foo()
foo_ref = weakref.ref(foo)
print(foo_ref)
print(foo_ref())
print(foo_ref() is foo)

foo = None
print(foo_ref())

foo_ref = None
print(foo_ref())

# Test weakref.WeakKeyDictionary()

class Foo(object):
    pass

foo = Foo()
foo_dict = weakref.WeakKeyDictionary()
foo_dict[foo] = 'foo'
print(foo_dict[foo])

foo = None
print(foo_dict)

foo_dict = None
print(foo_dict)

# Test weakref.WeakValueDictionary()

class Foo(object):
    pass

foo = Foo()
foo_dict = weakref.WeakValueDictionary()
foo_dict['foo'] = foo
print(foo_dict['foo'])

foo = None
print(foo_dict)

foo_dict = None
print(foo_dict)
