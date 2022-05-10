import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#import gc, weakref
#gc.set_debug(gc.DEBUG_COLLECTABLE)
#l = []
#l.append(weakref.proxy(l))
#gc.collect()
