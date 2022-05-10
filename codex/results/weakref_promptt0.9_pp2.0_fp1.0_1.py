import weakref
# Test weakref.ref to a function private value.

# Create the reference object
wr = weakref.ref(lambda: 42)
f = wr()
print f()
