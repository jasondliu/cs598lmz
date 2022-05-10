import weakref
# Test weakref.ref()

class Foo:
    pass

foo = Foo()
foo_ref = weakref.ref(foo)
foo_ref() is foo

foo = None
foo_ref() is None

foo = Foo()
foo_ref() is foo

foo_ref = None
foo = None
# Test weakref.WeakKeyDictionary()

class Foo:
    pass

foo = Foo()
weak_key_dict = weakref.WeakKeyDictionary()
weak_key_dict[foo] = 'bar'

foo = None
weak_key_dict

foo = Foo()
weak_key_dict[foo] = 'baz'

weak_key_dict

weak_key_dict = None
foo = None
# Test weakref.WeakValueDictionary()

class Foo:
    pass

foo = Foo()
weak_value_dict = weakref.WeakValueDictionary()
weak_value_dict['foo'] = foo

foo = None
weak_value_dict

foo = Foo()
weak_value_dict['foo'] = foo


