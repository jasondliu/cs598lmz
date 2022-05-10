import weakref
# Test weakref.ref()

class Foo:
    pass

foo = Foo()
foo_ref = weakref.ref(foo)

print(foo_ref)
print(foo_ref())

del foo
print(foo_ref())

# Test weakref.WeakKeyDictionary()

class Foo:
    pass

foo = Foo()

weak_dict = weakref.WeakKeyDictionary()
weak_dict['foo'] = 'bar'

print(weak_dict)
print(weak_dict['foo'])

del foo
print(weak_dict)

# Test weakref.WeakValueDictionary()

class Foo:
    pass

foo = Foo()

weak_dict = weakref.WeakValueDictionary()
weak_dict['foo'] = 'bar'

print(weak_dict)
print(weak_dict['foo'])

del foo
print(weak_dict)

# Test weakref.WeakSet()

class Foo:
    pass

foo = Foo()

weak_set = weakref.WeakSet()
weak_set.add
