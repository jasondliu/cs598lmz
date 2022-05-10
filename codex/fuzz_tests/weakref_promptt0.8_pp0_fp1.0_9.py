import weakref
# Test weakref.ref(Subclass)
class A(object): pass
class B(A): pass
class C(B): pass

a = A()
b = B()
c = C()

# References to (subclasses of) built-in types are not supported.
#test_support.run_doctest(weakref, verbose)

# Test weakref with a custom class.
class Foo(object):
    pass

class Bar(Foo):
    pass

def Get(name):
    return globals()[name]

r = weakref.ref(Foo)
assert r().__name__ == "Foo"
assert r().__class__ is type
assert weakref.ref(Foo)() is Foo
assert weakref.ref(Foo)() is Foo

assert weakref.ref(Bar)() is Bar
assert weakref.ref(Bar)() is Bar

# Test weakref with a classic class.
class ClassicFoo:
    pass

class ClassicBar(ClassicFoo):
    pass

assert weakref.ref(ClassicFoo)() is
