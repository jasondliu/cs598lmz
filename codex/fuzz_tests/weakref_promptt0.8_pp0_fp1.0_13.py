import weakref
# Test weakref.ref() with a non-weakable objec

class MyObject:
    pass

# Get a reference to MyObject
x = MyObject()

# Record the object id
x_id = id(x)

# Create a weak reference to the object
x_ref = weakref.ref(x)

# Check type of reference
print("Type of x_ref is " + str(type(x_ref)))

# Check if weak reference is still valid
if x_ref() is not None:
    print("Object 'x' referenced by weak reference is still alive")
    print("Type of the object referenced by weak reference is " + str(type(x_ref())))
else:
    print("Object 'x' referenced by weak reference is gone")

# Delete x. No more reference to x
del x

# Check if weak reference is still valid
if x_ref() is not None:
    print("Object 'x' referenced by weak reference is still alive")
    print("Type of the object referenced by weak reference is " + str(type(x_ref())))
else:
    print
