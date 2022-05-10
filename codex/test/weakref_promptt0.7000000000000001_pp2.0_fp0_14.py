import weakref
# Test weakref.ref()
import weakref

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%s)' % self.name

a = Foo('a')              # Create a reference
wr = weakref.ref(a)       # Create a weak reference
