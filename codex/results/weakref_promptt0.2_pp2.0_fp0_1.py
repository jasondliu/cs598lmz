import weakref
# Test weakref.ref()

class Foo(object):
    pass

f = Foo()

# Create a weak reference to f
r = weakref.ref(f)

# Print the object referred to by the weak reference
print r()

# Delete the object
del f

# Print the object referred to by the weak reference
print r()

# Test weakref.proxy()

class Foo(object):
    pass

f = Foo()

# Create a weak reference to f
r = weakref.proxy(f)

# Print the object referred to by the weak reference
print r

# Delete the object
del f

# Print the object referred to by the weak reference
print r

# Test weakref.WeakKeyDictionary()

class Foo(object):
    pass

f = Foo()

# Create a weak reference to f
r = weakref.WeakKeyDictionary()

# Print the object referred to by the weak reference
print r

# Delete the object
del f

# Print the object referred to by the weak reference
print r

# Test weakref.Weak
