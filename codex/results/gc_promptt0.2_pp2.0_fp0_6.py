import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%s)' % self.name

def bar():
    print('in bar')
    a = Foo('a')
    b = Foo('b')
    a.b = b
    b.a = a
    print('leaving bar')

bar()
print(gc.collect())
print(gc.garbage)

# Test gc.get_objects()

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%s)' % self.name

def bar():
    print('in bar')
    a = Foo('a')
    b = Foo('b')
    a.b = b
    b.a = a
    print('leaving bar')

bar()
print(gc.get_objects())

# Test gc.get_referrers()

class Foo
