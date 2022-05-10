import weakref
# Test weakref.ref() and weakref.proxy()

# Create a class with a __del__ method.
class Foo:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print('Foo.__del__(%s)' % self.name)

# Create a Foo instance.
f = Foo('f')

# Create a reference to f.
r = weakref.ref(f)

# Create a proxy to f.
p = weakref.proxy(f)

# Test the proxy.
print(p.name)

# Delete f.
del f

# See if the proxy is still usable.
try:
    print(p.name)
except ReferenceError:
    print('ReferenceError')

# See if the reference is still usable.
try:
    print(r().name)
except ReferenceError:
    print('ReferenceError')

# See if the reference is still usable.
try:
    print(r().name)
except ReferenceError:
    print('ReferenceError')

# See if the reference
