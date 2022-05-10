import weakref
# Test weakref.ref(None)
#
# Note: this test checks that weakref.ref(None) doesn't raise an exception.
# It doesn't test if the returned object is NULL or not.

print(weakref.ref(None) is None)
