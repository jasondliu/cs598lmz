import weakref
# Test weakref.ref(None)
wr = weakref.ref(None)
wr2 = weakref.ref(None, lambda: None)
# Check state of refs
wr()
wr2()
wr is wr2
wr() is wr2()
# Test weakref.ref(WrongType)
# Try to construct a weak reference to a class
wr = weakref.ref(WrongType())
# Check state of ref
wr()
# Try to construct a weak reference to a dynamic type
wr = weakref.ref(Record())
# Check state of ref
wr()
# Construct a weak reference to a dynamic type
wr = weakref.ref(Record())
# Find memory address of referent
repr(wr())
repr(wr)
# Access attribute of referent
wr().x
# call method of referent
wr().foo(2, None)
# Check state of ref
wr()
# Delete the referent
del wr().x
# Check state of ref
wr()
# Create second reference to referent
# (different from the original reference)
wr2 = weakref.ref(wr())
#
