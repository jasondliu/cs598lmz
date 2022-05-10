import weakref
# Test weakref.ref( x1, x2, x3, ...)
#       -> weakref.ref(x1, x2, x3, ...)
#
# The first argument is the referent.  All other arguments are
# callbacks that will be called when the referent is about to be
# collected.
#
# See also: weakref_ref_basic.py

#==============================================================================

# Create a class to use as referent
class Foo:
  x = 1

# Create a Foo object
f = Foo()

# Create a weak reference to the Foo object
# with the specified callbacks
ref1 = weakref.ref(f, lambda a: print("foobar"))

# Create another weak reference to the Foo object
# with the specified callbacks
ref2 = weakref.ref(f, lambda a: print("foobar2"))

#==============================================================================

print("Delete the Foo object")
# Delete the Foo object
del f

# Validate that the weak references are valid
# for an object that has been deleted

print("ref1() = ", ref1())
print
