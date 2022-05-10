import weakref
# Test weakref.ref(list)
#
# Weakrefs to lists are always dead, but the list shouldn't be freed
# immediately.

# Create a list.
l = []

# Create a weakref to it.
wr = weakref.ref(l)

# Delete the original object.
del l

# Check if the weakref is dead.
print wr() is None

# Check if the list has been garbage collected.
try:
    print wr()
except ReferenceError:
    pass
