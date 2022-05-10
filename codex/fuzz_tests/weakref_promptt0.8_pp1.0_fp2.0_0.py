import weakref
# Test weakref.ref, weakref.proxy

# Make some objects to work with
a = []
b = []
del a
del b

# Create a weak reference to a list
a = [1, 2, 3]
x = weakref.ref(a)
if x() is not a:
    raise TestFailed, "x() did not return original list"
if x() is not x():
    raise TestFailed, "x() did not return original list"
if x() is not x():
    raise TestFailed, "x() did not return original list"

# Create a weak reference to a function
def f():
    pass
y = weakref.ref(f)
if y() is not f:
    raise TestFailed, "y() did not return original function"

# Create a weak reference to a type
z = weakref.ref(int)
if z() is not int:
    raise TestFailed, "y() did not return original type"

# Create a weak dictionary
d = weakref.WeakValueDictionary()
if d.data is not None:
    raise
