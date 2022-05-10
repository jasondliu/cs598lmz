import weakref
# Test weakref.ref

# Create a class that implements __repr__
class C(object):
    pass

c = C()
c.__repr__ = lambda self: "<C instance>"

# Create a weak reference to the instance
r = weakref.ref(c)

# Verify that the weak reference works
print r() is c
print r()
print r().__repr__()

# Clear the weak reference
c = None

# Verify that the weak reference is dead
print r() is None

# Clear the original reference
r = None

# Create a weak reference to a class instance
class C(object):
    pass

c = C()
r = weakref.ref(c)

# Clear the original reference
c = None

# Verify that the weak reference is dead
print r() is None

# Create a weak reference to a function
def f():
    pass

r = weakref.ref(f)

# Clear the original reference
f = None

# Verify that the weak reference is dead
print r() is None
