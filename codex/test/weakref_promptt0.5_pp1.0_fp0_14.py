import weakref
# Test weakref.ref(x, f)
class Foo(object):
    def __init__(self, name):
        self.name = name

