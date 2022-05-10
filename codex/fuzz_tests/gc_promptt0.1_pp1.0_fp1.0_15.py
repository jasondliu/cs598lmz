import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%s)' % self.name

class Bar:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Bar(%s)' % self.name

def f():
    f1 = Foo('f1')
    f2 = Foo('f2')
    f3 = Foo('f3')
    f4 = Foo('f4')
    f5 = Foo('f5')
    f6 = Foo('f6')
    f7 = Foo('f7')
    f8 = Foo('f8')
    f9 = Foo('f9')
    f10 = Foo('f10')
    f11 = Foo('f11')
    f12 = Foo('f12')
    f13 = Foo('f13')
    f14 = Foo('f14')
    f15 = Foo('f15')
    f16 = Foo
