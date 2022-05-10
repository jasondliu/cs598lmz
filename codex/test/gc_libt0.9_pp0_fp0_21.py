import gc, weakref, types, sys, functools

GC_DEBUG = False

class object_exists:
    def __init__(self, thing):
        self.thing = thing
        
    def __enter__(self):
        return self.thing
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        #gc.collect()
        #return self.thing in gc.get_objects()
        del self.thing
        if gc.is_tracked(self.thing):
            del self.thing
            print(sys.getrefcount(self.thing))
            return False
        return True

def proxy(thing, name):
    class Proxy(object):
        def __init__(self):
            self.target = thing
            self.func = thing.__getattribute__(name)
            self.name = name
            self.ref = weakref.ref(self.target)
            functools.update_wrapper(self, thing)
            
