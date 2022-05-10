import gc, weakref

#------------------------------------------------------------------------------

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        return isinstance(other, Foo) and self.name == other.name

class Bar(object):
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        return isinstance(other, Bar) and self.name == other.name

#------------------------------------------------------------------------------

