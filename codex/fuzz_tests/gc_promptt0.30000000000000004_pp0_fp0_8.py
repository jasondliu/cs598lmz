import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback

class C(object):
    def __init__(self, callback):
        self.callback = callback
    def __del__(self):
        self.callback(self)

def callback(obj):
    print 'callback called'

def main():
    obj = C(callback)
    obj_ref = weakref.ref(obj, callback)
    del obj
    gc.collect()

main()
