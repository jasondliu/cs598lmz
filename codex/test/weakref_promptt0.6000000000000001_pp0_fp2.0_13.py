import weakref
# Test weakref.ref
class Foo(object): pass
foo = Foo()
r = weakref.ref(foo)
foo

# Test weakref.WeakKeyDictionary
d = weakref.WeakKeyDictionary()
d[foo] = 42
foo
d

# Test weakref.WeakValueDictionary
d = weakref.WeakValueDictionary()
d[42] = foo
foo
d

# Test weakref.WeakSet
s = weakref.WeakSet()
s.add(foo)
foo
s

# Test weakref.finalize
foo = Foo()
foo_ref = weakref.ref(foo)
def callback(foo_ref):
    print("Foo is dying")
weakref.finalize(foo, callback, foo_ref)
foo = None
foo_ref

# Test weakref.proxy
foo = Foo()
foo_ref = weakref.proxy(foo)
foo_ref.attr = 42
foo_ref.attr
foo
foo_ref
foo = None
foo_ref

# Test weakref.getweakrefcount
