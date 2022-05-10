import weakref
# Test weakref.ref()

class Foo:
    pass

f = Foo()

# Create a weak reference to f
r = weakref.ref(f)

# Print the object referred to by the weak reference
print(r())

# Delete the object
del f

# Print the object referred to by the weak reference
print(r())

# Create a weak reference to a list
r = weakref.ref([1, 2, 3])

# Print the object referred to by the weak reference
print(r())

# Delete the object
del r

# Print the object referred to by the weak reference
print(r())

# Create a weak reference to a list
r = weakref.ref([1, 2, 3])

# Print the object referred to by the weak reference
print(r())

# Delete the object
del r

# Print the object referred to by the weak reference
print(r())

# Create a weak reference to a list
r = weakref.ref([1, 2, 3])

# Print the object referred to by the weak reference
print(r())

#
