import weakref
# Test weakref.ref()

l = []
d = {}

class C:
    pass

l.append(C())   # l is a list of strong references to C instances.
d[0] = C()      # The dictionary d has a strong reference.

# These are all weak references to the same object.
wr = weakref.ref(C())
wf = weakref.ref(l[0])
wd = weakref.ref(d[0])

print(wr())  # An instance of C
print(wf())  # An instance of C
print(wd())  # An instance of C

# Remove the strong references
del l, d

print(wr())  # An instance of C
print(wf())  # None
print(wd())  # None

# Using a weak reference to break a reference cycle

class ExpensiveObject:
    def __del__(self):
        print('(Deleting %s)' % self)

def callback(reference):
    """Invoked when referenced object is deleted"""
    print('callback(', reference, ')')


