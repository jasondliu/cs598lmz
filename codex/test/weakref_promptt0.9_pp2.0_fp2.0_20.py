import weakref
# Test weakref.ref works on a C structure with a dict
# Note:  This is not a good weakrefable type, since a normal dict
# gets a hash, which is used by the weakref to index into the weakref list.
# This test overrides the hash and eq methods so that the test works
# on this type.  This can be done, in general, but the result is
# not reliable, since the hash value might be used for other things.

class MyStruct:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return self.x

    def __eq__(self, rhs):
        return self.x == rhs.x and self.y == rhs.y

class MyClass:
    def __init__(self):
        pass

