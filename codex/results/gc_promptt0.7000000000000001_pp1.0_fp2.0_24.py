import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on collectable objects.

def check_callback(unused):
    raise RuntimeError

print('Test gc.collect() on collectable objects... ', end='')

class X(object):
    def __del__(self):
        pass

class Y(X):
    def __del__(self):
        pass

w = weakref.ref(X(), check_callback)
x = X()
y = Y()

print('done.')
