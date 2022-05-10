import weakref
# Test weakref.ref.__repr__.
import sys
import weakref

class Foo(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<%s>" % (self.name,)


class Bar(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<%s>" % (self.name,)


class Baz(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<%s>" % (self.name,)


class Foo2(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<%s>" % (self.name,)


class Bar2(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<%s>" % (self.name,)
