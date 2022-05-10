import weakref
# Test weakref.ref

class Foo:
    pass

f = Foo()

r = weakref.ref(f)

print(r)
print(r())
print(r() is f)
print(r() is None)

f = None
print(r() is None)

print(r())

# Reference to a non-weakrefable object
r = weakref.ref(1)
print(r())

# Reference to an object that is not alive
class Foo:
    pass

a = Foo()
b = Foo()
a.b = b
b.a = a
del a
del b

r = weakref.ref(Foo.__dict__)
print(r())

# Reference to an object that is not alive
class Foo:
    pass

a = Foo()
b = Foo()
a.b = b
b.a = a
del a
del b

r = weakref.ref(Foo.__dict__)
print(r())

# Reference to an object that is not alive
class Foo:
    pass

a
