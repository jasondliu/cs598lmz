import gc, weakref

class Foo:
    def __init__(self, name):
        self.name = name
        print('Created a Foo object with name', name)

    def __del__(self):
        print('Deleting a Foo object with name', self.name)


def bye():
    print('Gone with the wind...')

# Create a Foo instance
f = Foo('Leo')

# Create a weak reference to f
# wref = weakref.ref(f, bye)
wref = weakref.ref(f)

# Delete the Foo instance
del f

# Print the weak reference
print('wref:', wref)

# Print the object the weak reference refers to
print('wref():', wref())

# Print the object the weak reference refers to
