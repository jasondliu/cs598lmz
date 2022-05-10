import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect(): the created frames should be cleaned up,
# even if we've kept a reference to the function object
def create_frames(func):
    for i in range(10):
        func(i)
def func(i):
    frame = sys._getframe()
f = func
create_frames(func)
gc.collect()
del func
gc.collect()
