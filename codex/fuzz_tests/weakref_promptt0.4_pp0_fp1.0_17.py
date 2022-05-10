import weakref
# Test weakref.ref() and weakref.proxy()

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%s)' % self.name

class Bar(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Bar(%s)' % self.name

class FooBar(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'FooBar(%s)' % self.name

class FooBar2(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'FooBar2(%s)' % self.name

class FooBar3(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'FooBar3(%
