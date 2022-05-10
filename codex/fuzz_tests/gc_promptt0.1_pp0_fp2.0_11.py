import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%s)' % self.name

def show_refs(message, *objects):
    print(message)
    for obj in objects:
        print('  object:', obj)
        print('  referred:', gc.get_referents(obj))

a = Foo('a')
b = Foo('b')
c = Foo('c')

show_refs('initial:', a, b, c)

a = b = c = None

show_refs('collected:', gc.collect())

# Test gc.garbage

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%s)' % self.name

def show_garbage():
    print('garbage:', gc.garbage)

show_garbage()

a =
