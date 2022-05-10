import gc, weakref

class Bar:
    def __init__(self, n):
        self.bar = n
        self.obj = weakref.ref(self)

    def __repr__(self):
        return '<Bar {0.bar}>'.format(self)

class Foo(object):

    def __init__(self):
        self.obj = weakref.ref(self)

    def create(self, n = 5):
        self.bar = Bar(n)
        self.bar.obj = self
        self.bar.parent = weakref.ref(self)
        self.bar.parent1 = weakref.proxy(self)
        self.bar.parent2 = weakref.ref(self.bar.parent2)
        self.bar.parent3 = weakref.proxy(self.bar.parent3)
        self.bar.parent4 = weakref.ref(self.bar.parent4)
        self.bar.parent5 = weakref.proxy(self.bar.parent5)
