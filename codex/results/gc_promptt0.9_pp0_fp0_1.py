import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with a finalizer that has to resurrect a finalizer (bug 1059955).
def f(obj):
    print('Alive!')
    lastref = obj.aliveref
obj = C()
refs = [weakref.ref(obj)]
obj.aliveref = refs[-1]
