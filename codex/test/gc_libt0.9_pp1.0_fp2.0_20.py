import gc, weakref, contextlib

gc.set_debug(gc.DEBUG_UNCOLLECTABLE)


def weakref_callback(obj, data=None):
    if data is not None:
        print(data)
    obj = None

print('Child:')
