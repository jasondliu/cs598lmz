import weakref
# Test weakref.ref(obj)

# Create an object
class A(object):
    pass

a = A()

# Create a weak reference to the object
r = weakref.ref(a)

# Print the weak reference
print('r = {!r}'.format(r))

# Print the object referred to
print('r() = {!r}'.format(r()))

# Delete the object
del a

# Print the weak reference
print('r = {!r}'.format(r))

# Print the object referred to
print('r() = {!r}'.format(r()))

# Create a weak reference to the object
r = weakref.ref(a)

# Print the weak reference
print('r = {!r}'.format(r))

# Print the object referred to
print('r() = {!r}'.format(r()))

# Delete the object
del a

# Print the weak reference
print('r = {!r}'.format(r))

# Print the object referred to
print('r() = {!r
