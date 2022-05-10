import weakref
# Test weakref.ref() and weakref.proxy()

# This is a very simple test case.  It doesn't test all the edge cases
# that need to be tested.

class C:
    pass

# Create a strong reference
c = C()

# Create a weak reference
w = weakref.ref(c)

# Create a weak proxy
p = weakref.proxy(c)

