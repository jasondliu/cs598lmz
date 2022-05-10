import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return '<%s object, name=%r>' % (self.__class__.__name__, self.name)

def show_refs(message, refs):
    print message
    for ref in refs:
        obj = ref()
        if obj is not None:
            print '  object', obj
        else:
            print '  dead'

print 'Setting up'
f = Foo('f')
d = {'1': f}
l = [f]
wr = weakref.ref(f)
show_refs('initial:', [wr])

print 'Deleting f from scope'
del f
show_refs('scope cleared:', [wr])

print 'Forcing garbage collection'
gc.collect()
show_refs('after gc:', [wr])

print 'Deleting remaining references'
del d
del l
gc.collect()
show_
