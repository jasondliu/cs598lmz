import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'A(%s)' % self.name

class B:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'B(%s)' % self.name

class C:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'C(%s)' % self.name

class D:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'D(%s)' % self.name

class E:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'E(%s)' % self.name

class F:
    def __init__(self, name):
        self.name = name

