import weakref
# Test weakref.ref() on an object with a __del__ method.
class MyObject(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'MyObject(%r)' % self.name

