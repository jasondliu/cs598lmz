import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(' + self.name + ')'
    def __del__(self):
        print 'deleting', self

f = Foo('f')
fwr = weakref.ref(f)
print fwr()
del f
print fwr()
gc.collect()
print fwr()

# Test gc.garbage
class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(' + self.name + ')'
    def __del__(self):
        print 'deleting', self

f = Foo('f')
fwr = weakref.ref(f)
print fwr()
del f
print fwr()
print gc.garbage

# Test gc.get_objects()
class Foo:
    def __init__(self, name):
        self.name = name
    def
