import weakref
# Test weakref.ref(obj, callback)

class Foo:
    pass

def callback(ref):
    print('callback called')

foo = Foo()
f = weakref.ref(foo, callback)
print(f)
print(f())
del foo
print(f())
print(f)

# Test weakref.ref(obj)

class Foo:
    pass

foo = Foo()
f = weakref.ref(foo)
print(f)
print(f())
del foo
print(f())
print(f)

# Test weakref.ref(obj, callback) with a class instance

class Foo:
    def __init__(self):
        self.bar = 'bar'

def callback(ref):
    print('callback called')

foo = Foo()
f = weakref.ref(foo, callback)
print(f)
print(f().bar)
del foo
print(f())
print(f)

# Test weakref.ref(obj) with a class instance

class Foo:
    def __init__(self):
        self
