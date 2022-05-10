import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class Foo(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%s)' % self.name

class Bar(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Bar(%s)' % self.name

a = Foo('a')
b = Bar('b')
a.b = b
b.a = a
# Test gc.collect()
import gc
gc.collect()
# Test gc.get_objects()
import gc
gc.get_objects()
# Test gc.get_referrers()
import gc
gc.get_referrers(a)
# Test gc.get_referents()
import gc
gc.get_referents(a)
# Test gc.is_tracked()
import gc
gc.is_tracked(a)
# Test gc.is_tracked()
import g
