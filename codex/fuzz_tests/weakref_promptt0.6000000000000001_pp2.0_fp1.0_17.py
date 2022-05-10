import weakref
# Test weakref.ref(obj, callback)
#
# Make sure that the callback is called when the object is garbage collected
# and that the callback isn't called when the reference object is garbage
# collected.

class Object:
    def __init__(self, id):
        self.id = id
    def __repr__(self):
        return '<Object %s>' % self.id

def callback(obj):
    print 'callback:', obj
    callback.called = 1

callback.called = 0

# Test with a function
a = Object('a')
aref = weakref.ref(a, callback)
a = None
gc.collect()
assert callback.called

# Test with a class
class A:
    def __init__(self, id):
        self.id = id
    def __repr__(self):
        return '<A %s>' % self.id

a = A('a')
aref = weakref.ref(a, callback)
a = None
gc.collect()
assert callback.called

# Test with an instance method

