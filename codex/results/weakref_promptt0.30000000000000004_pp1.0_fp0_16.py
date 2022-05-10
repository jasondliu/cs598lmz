import weakref
# Test weakref.ref() and weakref.proxy()

class Foo:
    pass

f = Foo()

# Create a weak reference to f
r = weakref.ref(f)

# Create a weak proxy to f
p = weakref.proxy(f)

# Print the object referred to by r
print(r())

# Print the object referred to by p
print(p)

# Delete f
del f

# Print the object referred to by r
print(r())

# Print the object referred to by p
print(p)

# Create a weak reference to the list [1, 2, 3]
r = weakref.ref([1, 2, 3])

# Create a weak proxy to the list [1, 2, 3]
p = weakref.proxy([1, 2, 3])

# Print the object referred to by r
print(r())

# Print the object referred to by p
print(p)

# Delete the list [1, 2, 3]
del p

# Print the object referred to by r
print(r())

# Print the
