import weakref
# Test weakref.ref()
# Create a class with a __del__ method
class Foo(object):
    def __del__(self):
        print "deleted"

# Create an instance of Foo
f = Foo()

# Create a weak reference to f
r = weakref.ref(f)

# Print the object referred to by the weak reference
print r()

# Delete f
del f

# Print the object referred to by the weak reference
print r()

# Test weakref.finalize()
# Create a class with a __del__ method
class Foo(object):
    def __del__(self):
        print "deleted"

# Create an instance of Foo
f = Foo()

# Create a weak reference to f
r = weakref.finalize(f, print, "deleted")

# Print the object referred to by the weak reference
print r.alive

# Delete f
del f

# Print the object referred to by the weak reference
print r.alive

# Test weakref.WeakKeyDictionary()
# Create a class with a __del__ method
