import gc, weakref

class MyClass(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'MyClass(%s)' % self.name

gc.set_debug(gc.DEBUG_SAVEALL)

o = MyClass('instance')
wref = weakref.ref(o)

