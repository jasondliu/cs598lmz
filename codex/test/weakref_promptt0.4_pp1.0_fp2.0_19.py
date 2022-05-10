import weakref
# Test weakref.ref(obj)

class Foo(object): pass

foo = Foo()
foo.bar = Foo()

