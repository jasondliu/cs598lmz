import weakref
# Test weakref.ref(foo) is foo
# Test weakref.ref(foo)() is foo

class Foo:
    pass

f = Foo()

r = weakref.ref(f)
if r() is not f:
    print("Error: r() is not f")

if r is not f:
    print("Error: r is not f")
