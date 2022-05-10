import weakref
# Test weakref.ref method
# Weak reference to a list
a = [10, 20, 30]
b = weakref.ref(a)     # b is a weak reference to list a
# Del variable a
del a
# Try access variable b
print(b())             # b() returns the referred object
# List is deleted from memory
# Try b.append(40)
# b.append(40)
# Output: AttributeError
