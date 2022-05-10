import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() does the right thing for weakrefs whose callback
# methods have direct cycles with the objects they're weakref-ing.

def callback(wr, self=weakref.ref(None)):
    self().foo = 'bar'

class MyObj(object):
    def __init__(self, callback):
        self.wr = weakref.ref(self, callback)

class MySubclass(MyObj):
    pass

def main():
    obj = MyObj(lambda x: callback(x, self=weakref.ref(obj)))
    obj2 = MySubclass(lambda x: callback(x, self=weakref.ref(obj2)))

    for obj in [obj, obj2]:
        if not obj.wr():
            raise RuntimeError("The weak reference was lost too soon!")
        del obj

    #print gc.collect(); print
    #print gc.garbage[0]
    #print gc.garbage[1]
    ref = gc.garbage[0]
    if ref.__class__ is MyObj:
        ref = g
