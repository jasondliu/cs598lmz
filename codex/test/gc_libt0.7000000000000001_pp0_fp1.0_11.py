import gc, weakref

gc.enable()
gc.set_debug(gc.DEBUG_LEAK)



class ToBeCollected:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'ToBeCollected(%s)' % self.name


def demo():
    obj = ToBeCollected('obj')
    ref = weakref.ref(obj)
