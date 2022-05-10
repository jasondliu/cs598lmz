import weakref
# Test weakref.ref(obj)

class A:
    pass

a = A()

# Create a weak reference to a
r = weakref.ref(a)

# Print the reference
print('Object referred to:', r())

# Delete the object
del a

# Print the reference
print('Object referred to:', r())

# Test weakref.getweakrefcount(obj)

class A:
    pass

a = A()

# Create a weak reference to a
r = weakref.ref(a)

# Print the number of weak references to a
print('Number of weak references:', weakref.getweakrefcount(a))

# Delete the object
del a

# Print the number of weak references to a
print('Number of weak references:', weakref.getweakrefcount(r))

# Test weakref.getweakrefs(obj)

class A:
    pass

a = A()

# Create a weak reference to a
r = weakref.ref(a)

# Print the weak references to a
print('Weak references:
