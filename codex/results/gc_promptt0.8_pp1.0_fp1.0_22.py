import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect

# Here's an object with a __del__ method that just prints a message.
class H(object):
    def __init__(self, n):
        self.n = n
    def __repr__(self):
        return 'H(%r)' % self.n
    def __del__(self):
        print 'deleting H(%r)' % self.n

# Create a cycle.
a = H(1)
b = H(2)
a.x = b
b.x = a

# Check that it's a cycle.
print 'Cycle:'
gc.collect()
print

# Break the cycle.
print 'Breaking cycle...',
a.x = None
b.x = None
print 'success'

# Check that __del__ was called.
print 'Collecting...',
gc.collect()
print 'success'

# Create a cycle and make it unreachable.
a = H(1)
b = H(2)
a.x = b
b.x = a

# Check that it's a cycle.

