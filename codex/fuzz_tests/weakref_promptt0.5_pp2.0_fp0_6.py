import weakref
# Test weakref.ref()

# Create an object
class Test:
    pass

test = Test()

# Create a weak reference to the object
r = weakref.ref(test)

# Print the weak reference
print(r)

# Print the object referred to by the weak reference
print(r())

# Delete the object
del test

# Print the weak reference
print(r)

# Print the object referred to by the weak reference
print(r())
# Test weakref.WeakValueDictionary()

# Create an object
class Test:
    pass

test = Test()

# Create a weak value dictionary
d = weakref.WeakValueDictionary()

# Add the object to the dictionary
d['test'] = test

# Print the dictionary
print(d)

# Print the dictionary keys
print(d.keys())

# Print the dictionary values
print(d.values())

# Print the dictionary items
print(d.items())

# Delete the object
del test

# Print the dictionary
print(d)

# Print the dictionary keys
print(
