import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a simple finalizer:
print('Testing base class...')
class NoFinalizer(object):
    def __init__(self):
        self.children = []
    def addchild(self, child):
        self.children.append(child)
    def delchild(self, child):
        self.children.remove(child)
    def __repr__(self):
        return '<gctest %r at %#x>' % (self.children, id(self))

class Finalizer(NoFinalizer):
    def __del__(self):
        print('Finalizer.__del__ called on', self)
        self.check_num_children()

class FinalizerCheck(NoFinalizer):
    def __del__(self):
        self.check_num_children()
    def check_num_children(self):
        print('Union for', self)
        for child in self.children:
            print('Union:', child)

class FinalizerRoot(NoFinalizer):
    def __del__(self):
        self.check_num_
