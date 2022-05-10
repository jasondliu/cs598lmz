import weakref
# Test weakref.ref() by comparing it to the object to which is refers
ref = weakref.ref(5)
print(ref == 5)
# Test weakref.ref() by comparing it to an object it does not refer to
print(ref == 6)
# Test the object to which weakref.ref() refers to is still alive
print(ref() == 5)
