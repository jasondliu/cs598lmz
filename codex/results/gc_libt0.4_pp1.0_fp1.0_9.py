import gc, weakref

class Foo:
    def __init__(self, name):
        self.name = name
        print('Created a Foo object with name:', self.name)

    def __del__(self):
        print('Deleting a Foo object with name:', self.name)

def bar(name):
    return Foo(name)

f = bar('f')
b = bar('b')

# The reference count of f and b is 2
print('Reference count of f:', sys.getrefcount(f))
print('Reference count of b:', sys.getrefcount(b))

# The reference count of f and b is 1
w = weakref.ref(f)
print('Reference count of f:', sys.getrefcount(f))
print('Reference count of b:', sys.getrefcount(b))

# The reference count of f and b is 1
del f
print('Reference count of b:', sys.getrefcount(b))

# The reference count of f and b is 1
f = w()
print('Reference count of f:',
