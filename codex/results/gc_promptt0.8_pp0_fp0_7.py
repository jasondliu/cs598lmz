import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a collectable object that has finalizers
import gc
import weakref

class Collectable(object):
    def __init__(self):
        self.ref = weakref.ref(self, lambda wr: self.__finalize__())
    def __finalize__(self):
        #print 'finalizing'
        self.ref = None

def run():
    c = Collectable()
    c.x = c
    c.y = [c]
    #print 'collecting'
    gc.collect()
    #print 'collected'

weakref.finalize(None, run)

gc.collect()

# Test gc.collect() with a collectable object that has finalizers and weakrefs
import gc
import weakref

class Collectable(object):
    def __init__(self):
        self.ref = weakref.ref(self)
        self.wr = weakref.ref(self, lambda wr: self.__finalize__())

    def __finalize__(self):
        #print 'finalizing'
       
