import weakref
# Test weakref.ref()

class Foo:
    pass

def bar():
    pass

f = Foo()

print(weakref.ref(f))
print(weakref.ref(bar))

print(weakref.ref(f)())
print(weakref.ref(bar)())

print(weakref.ref(f) is weakref.ref(f))
print(weakref.ref(f) is not weakref.ref(bar))

print(weakref.ref(f) is weakref.ref(f)())
print(weakref.ref(f) is not weakref.ref(bar)())

print(weakref.ref(f)() is weakref.ref(f)())
print(weakref.ref(f)() is not weakref.ref(bar)())

print(weakref.ref(f)() is f)
print(weakref.ref(bar)() is bar)

print(weakref.ref(f)() is not bar)
print(weakref.ref(bar)() is not f)

print(weakref.ref
