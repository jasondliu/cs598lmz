import weakref
# Test weakref.ref(x) == weakref.ref(x)

class Foo:
    pass

foo1 = Foo()
foo2 = Foo()

ref1 = weakref.ref(foo1)
ref2 = weakref.ref(foo1)
ref3 = weakref.ref(foo2)

print(ref1 == ref2)
print(ref1 == ref3)
print(ref2 == ref3)

print(ref1 == foo1)
print(ref1 == foo2)
print(ref2 == foo1)
print(ref2 == foo2)
print(ref3 == foo1)
print(ref3 == foo2)

print(foo1 == ref1)
print(foo1 == ref2)
print(foo1 == ref3)
print(foo2 == ref1)
print(foo2 == ref2)
print(foo2 == ref3)

print(ref1 == None)
print(ref2 == None)
print(ref3 == None)

print(None == ref1)
print(None == ref2)
print(None == ref
