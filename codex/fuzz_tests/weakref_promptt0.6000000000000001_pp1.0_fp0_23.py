import weakref
# Test weakref.ref on a class with a custom __hash__ and __eq__.
import collections
class H(collections.Hashable):
    def __init__(self, x):
        self.x = x

    def __hash__(self):
        return hash(self.x)

    def __eq__(self, other):
        return self.x == other.x


class G(collections.Hashable):
    def __init__(self, x):
        self.x = x

    def __hash__(self):
        return hash(self.x)

    def __eq__(self, other):
        return self.x == other.x


def test_hashable_equality():
    a = H(1)
    b = H(1)
    c = G(1)
    assert a == b
    assert hash(a) == hash(b)
    assert a != c
    assert hash(a) != hash(c)
    d = weakref.ref(a)
    e = weakref.ref(b)
    f = weakref.ref(c)
