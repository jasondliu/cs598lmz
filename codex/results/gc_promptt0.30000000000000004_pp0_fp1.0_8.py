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

class FooBar:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'FooBar(%s)' % self.name

def show_refs(obj):
    print '%s refers to:' % obj
    for r in gc.get_referents(obj):
        print '  ', r

def show_backrefs(obj):
    print '%s is referred to by:' % obj
    for r in gc.get_referrers(obj):
        print '  ', r

def show_all_refs(obj):
    print '%s refers to:'
