import weakref
# Test weakref.ref() with a cyclic reference.
import _weakref

# A simple class to test weak references to objects with cyclic references to
# themselves.
# The cyclic reference is implemented by having an object maintain a list of all
# instances of the class.
class C:
  instances = []
  def __init__(self):
    self.instances.append(self)
    self.x = 1

  def ping(self):
    return "pong"

# Create an object with a cyclic reference to itself
c = C()

# Get a weak reference to the object
r = weakref.ref(c)

# Check that the weak reference can be dereferenced
print(r().ping())

# Check that the weak reference doesn't keep the object alive
del c
print(_weakref.is_dead(r))

# Check that the weak reference itself is gone when the last reference to it
# is deleted
r2 = r
del r
print(_weakref.is_dead(r2))
