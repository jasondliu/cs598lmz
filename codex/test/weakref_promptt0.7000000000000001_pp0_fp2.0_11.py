import weakref
# Test weakref.ref() on a list

# Initialize a list and a weak reference to the list
L = [1, 2, 3]
r = weakref.ref(L)

# Print the weak reference
print('Before:', r)

# Delete the original list
del L

# Print the weak reference
print('After:', r)
