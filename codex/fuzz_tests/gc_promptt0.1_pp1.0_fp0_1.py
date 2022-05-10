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
show_refs('initial:', a, b)

a_id = id(a)
b_id = id(b)

a = None
b = None

for o in gc.get_objects():
    if id(o) in (a_id, b_id):
        print('found uncollected:', o)

gc.collect()

for o in gc.get_objects():
    if id(o) in (a_id, b_id):
        print('found uncollected:', o)

# Test gc.get
