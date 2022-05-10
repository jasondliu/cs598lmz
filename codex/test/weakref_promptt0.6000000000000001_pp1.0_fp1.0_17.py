import weakref
# Test weakref.ref().

class Foo:

    def __init__(self, name):
        self.name = name
        self.refs = []

    def AddRef(self, r):
        self.refs.append(r)

