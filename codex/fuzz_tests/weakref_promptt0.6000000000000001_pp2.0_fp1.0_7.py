import weakref
# Test weakref.ref(obj, callback)

class Foo:
    pass

def callback(r):
    print('callback called')

foo = Foo()
f = weakref.ref(foo, callback)
print(f)
print(f())
del foo
print(f)
print(f())

print('-' * 40)

foo = Foo()
f = weakref.ref(foo)
print(f)
print(f())
del foo
print(f)
print(f())

print('-' * 40)

foo = Foo()
f = weakref.ref(foo)
print(f)
print(f())
del foo
print(f)
print(f())

print(f())

print('-' * 40)

foo = Foo()
f = weakref.ref(foo)
print(f)
print(f())
del foo
print(f)
print(f())

print(f())

print(f())

print('-' * 40)

foo = Foo()
f = weakref.ref(foo)
print(f
