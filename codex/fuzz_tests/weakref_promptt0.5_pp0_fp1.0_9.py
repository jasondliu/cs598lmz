import weakref
# Test weakref.ref

# Create a function that we can use to test weak references
def callback(reference):
    print 'callback(', reference, ')'

# Create an instance of a class with a __del__ method
class Object:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print '(Deleting %s)' % self

# Create a weak reference to the instance
o = Object('weakref test')
r = weakref.ref(o, callback)

print 'o:', o
print 'r:', r
print 'r():', r()
print 'deleting o'
del o
print 'r():', r()

# Test weakref.WeakValueDictionary

# Create an instance of a class with a __del__ method
class Object:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print '(Deleting %s)' % self

# Create a WeakValueDictionary, and add an object
d = weakref.WeakValueDictionary
