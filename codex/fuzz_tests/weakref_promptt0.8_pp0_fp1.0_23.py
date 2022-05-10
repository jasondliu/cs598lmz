import weakref
# Test weakref.ref(object)
m = weakref.ref(m)
print(m)

# Test a weakref to the same object.
# This should not make m a dangling reference.
m2 = weakref.ref(m)
print(m2)

# Test a weakref directly to a temporary.
m = {1:1, 2:2}
m = weakref.ref(m)
print(m)

# Test weakref.ReferenceType(object)
m = weakref.ReferenceType(m)
print(m)

# Test a weakref to the same object.
# This should not make m a dangling reference.
m2 = weakref.ReferenceType(m)
print(m2)
