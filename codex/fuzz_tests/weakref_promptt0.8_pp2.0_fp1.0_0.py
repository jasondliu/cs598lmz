import weakref
# Test weakref.ref(x); should *not* raise TypeError


class Foo:
    pass


class Foo2:

    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return self.x == other.x


class FooSub(Foo):
    pass


class Foo2Sub(Foo2):

    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return self.x == other.x


class Foo2Sub2(Foo2):

    def __init__(self, x):
        self.x = x


class Foo3(object):
    pass


class Foo3Sub(Foo3):
    pass


class Foo4(object):

    def __init__(self, x):
        self.x = x


class Foo4Sub(Foo4):

    def __init__(self, x):
        self.x = x


class TestWeakref:

    def test_basic(self):
        o =
