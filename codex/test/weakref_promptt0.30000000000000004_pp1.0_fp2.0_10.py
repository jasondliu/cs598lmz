import weakref
# Test weakref.ref()

class Foo(object):
    def __init__(self, name):
        self.name = name
