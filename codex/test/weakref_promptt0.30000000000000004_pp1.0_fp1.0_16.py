import weakref
# Test weakref.ref()

import weakref

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%r)' % self.name

