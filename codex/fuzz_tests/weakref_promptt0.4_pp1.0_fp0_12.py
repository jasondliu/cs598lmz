import weakref
# Test weakref.ref() with a callable object.

class Foo:
    def __init__(self, value):
        self.value = value
    def __call__(self):
        return self.value

def callback(r):
    print(r())

f = Foo(42)
r = weakref.ref(f, callback)
del f
print(r())
# Test weakref.ref() with a class instance.

class Foo:
    def __init__(self, value):
        self.value = value

def callback(r):
    print(r)

f = Foo(42)
r = weakref.ref(f, callback)
del f
print(r)
# Test weakref.ref() with a class instance and no callback.

class Foo:
    def __init__(self, value):
        self.value = value

f = Foo(42)
r = weakref.ref(f)
del f
print(r)
# Test weakref.ref() with an instance method.

class Foo:
    def __init__(self,
