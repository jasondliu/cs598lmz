import weakref
# Test weakref.ref()

class Foo:
    pass

f = Foo()
f.x = 1

# Create a reference to Foo()
r = weakref.ref(f)

# Print the id of Foo()
print(id(f))

# Print the id of the object that the weak reference points to
print(id(r()))

# Delete Foo()
del f

# Print the id of the object that the weak reference points to
print(id(r()))

# Print the id of the object that the weak reference points to
print(r())

# Print the id of the object that the weak reference points to
print(r() is None)

# Print the id of the object that the weak reference points to
print(r() is None)

# Print the id of the object that the weak reference points to
print(r() is None)

# Print the id of the object that the weak reference points to
print(r() is None)

# Print the id of the object that the weak reference points to
print(r() is None)

# Print the id of the object
