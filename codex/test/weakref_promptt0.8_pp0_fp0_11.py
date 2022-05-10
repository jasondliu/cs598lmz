import weakref
# Test weakref.ref()
# Create a class referencing an object
class C:
    def __init__(self, obj):
        self.obj = obj

# Create an object
x = 1234

# Create a reference to x
cref = C(x)
print(type(cref.obj))

# Create a weak reference to x
wref = weakref.ref(x)

# Create a strong reference to x
sref = x

# Delete all references to x
del x

# Nothing special here: ref still points to the old x.
print(cref.obj)
print(sref)

# Use of wref() raises an exception
try:
    wref()
except ReferenceError:
    print("wref could not be resolved")

# Test weakref.proxy()
class C:
    def __init__(self, obj):
        self.obj = obj

# Create an object
x = 1234

# Create a reference to x
cref = C(x)

# Create a weak reference to x
wref = weakref.proxy(x)
