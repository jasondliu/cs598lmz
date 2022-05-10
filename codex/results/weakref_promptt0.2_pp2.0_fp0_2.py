import weakref
# Test weakref.ref()

# Create a class with a method that prints the object's id
class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return "<Foo %s>" % self.name
    def show(self):
        print(id(self))

# Create a Foo instance
f = Foo('f')

# Create a weak reference to the Foo instance
r = weakref.ref(f)

# Print the id of the Foo instance
print(id(f))

# Print the id of the Foo instance through the weak reference
r().show()

# Delete the Foo instance
del f

# Print the id of the Foo instance through the weak reference
r().show()

# Print the id of the Foo instance through the weak reference
r().show()

# Print the id of the Foo instance through the weak reference
r().show()

# Print the id of the Foo instance through the weak reference
r().show()

# Print the id of the Foo instance through the weak reference
r().show()

#
