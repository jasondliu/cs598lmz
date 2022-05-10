import weakref
# Test weakref.ref(x) == weakref.ref(x)

class Foo:
    pass

foo = Foo()
bar = Foo()

ref1 = weakref.ref(foo)
ref2 = weakref.ref(foo)
ref3 = weakref.ref(bar)

print(ref1 == ref2)
print(ref1 == ref3)
print(ref2 == ref3)
print(ref1 == foo)
print(ref1 == bar)
print(ref2 == foo)
print(ref2 == bar)
print(ref3 == foo)
print(ref3 == bar)
