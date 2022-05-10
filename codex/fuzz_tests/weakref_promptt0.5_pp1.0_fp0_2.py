import weakref
# Test weakref.ref()
#
# The weakref module provides a standard interface for tracking objects
# without creating a reference that would keep them alive.  A weak
# reference to an object is not enough to keep the object alive: if no
# strong reference to the object exists, garbage collection is free to
# destroy the object and reuse its memory for something else.
#
# The weakref module provides two kinds of weak references:
#
#     - A "weakref" is a normal weak reference.  When the object
#       is garbage collected, the weak reference object becomes
#       dead, and accessing it returns None.
#
#     - A "proxy" is a weak reference that returns another object
#       when dereferenced.
#
# The following example creates a weak reference to a list; the list
# is created and then deleted, but the weak reference survives:

class Foo(object):
    pass

a = Foo()
d = weakref.ref(a) # Create a weak reference to a
d() is a

del a
d() is None

# The following example shows how to use a proxy to return a default
