import weakref
# Test weakref.ref() and weakref.proxy()
#
# This test also serves as a regression test for SF bug #813657
#
# We create a weak reference to a class instance, and verify that the
# weak reference can be used to access the class instance.
#
# We also create a weak reference to a class instance, and verify that
# the weak reference can be used to access the class instance via a
# weak proxy.
#
# We also verify that the weak reference dies when the class instance
# dies.
#
# We also verify that the weak proxy dies when the class instance
# dies.

class C:
    pass

c = C()

# Create a weak reference to c
w = weakref.ref(c)

# Verify that the weak reference can be used to access c
if w() is not c:
    raise TestFailed, "weak reference could not be used to access c"

# Create a weak proxy to c
p = weakref.proxy(c)

# Verify that the weak proxy can be used to access c
if p is not c:
    raise TestFailed,
