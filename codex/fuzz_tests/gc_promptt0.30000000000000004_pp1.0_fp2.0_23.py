import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    def __init__(self, name):
        self.name = name
        print('Created', self.name)
    def __del__(self):
        print('Deleted', self.name)

def test():
    a = Foo('a')
    b = Foo('b')
    c = Foo('c')
    a.b = b
    b.c = c
    c.a = a
    del a
    del b
    del c

test()
print('Collecting...')
gc.collect()
print('Done.')

# Test gc.get_objects()

class Foo:
    def __init__(self, name):
        self.name = name
        print('Created', self.name)
    def __del__(self):
        print('Deleted', self.name)

def test():
    a = Foo('a')
    b = Foo('b')
    c = Foo('c')
    a.b = b
    b.c = c
    c.a = a
    del
