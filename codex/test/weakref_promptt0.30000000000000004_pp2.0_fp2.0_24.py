import weakref
# Test weakref.ref(obj, callback)

import weakref

class C(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'C(%r)' % self.name

