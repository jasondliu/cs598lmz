import weakref
# Test weakref.ref(obj)

class Foo(object):
    def __init__(self, name):
        self.name = name
