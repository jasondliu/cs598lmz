import gc, weakref

# pylint: disable=too-many-public-methods,protected-access
# pylint: disable=too-many-instance-attributes

class TestObject(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "TestObject(%s)" % self.name

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self.name < other.name

    def __le__(self, other):
        return self.name <= other.name

    def __gt__(self, other):
        return self.name > other.name

    def __ge__(self, other):
        return self.name >= other.name

    def __hash__(self):
        return hash(self.name)

    def __reduce__(self):
        return TestObject, (self.name,)

