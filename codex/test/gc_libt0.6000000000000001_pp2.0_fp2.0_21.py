import gc, weakref

class B:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return 'B(%s)' % self.value

class C:
    def __init__(self):
        self.b = B(42)
    def __repr__(self):
        return 'C()'

