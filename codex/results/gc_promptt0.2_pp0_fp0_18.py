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
        print('  object %r from %r' % (obj, obj.__class__))
        if isinstance(obj, Foo):
            print('    %s' % obj.name)
    print()

# Create a bunch of objects, and show references
show_refs('Creating objects...',
          Foo('a'), Foo('b'), Foo('c'), Foo('d'))

# Collect the objects, and show what is left
gc.collect()
show_refs('After collecting', Foo('a'), Foo('b'), Foo('c'), Foo('d'))

# Create a cycle, and show what happens
a = Foo('a')
b = Foo('b')
a.other = b
b.other = a
show_refs('Creating a cycle', a
