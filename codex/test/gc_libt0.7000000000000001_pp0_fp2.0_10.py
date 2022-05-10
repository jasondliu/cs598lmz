import gc, weakref

class SomeClass(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'SomeClass(%s)' % self.name

