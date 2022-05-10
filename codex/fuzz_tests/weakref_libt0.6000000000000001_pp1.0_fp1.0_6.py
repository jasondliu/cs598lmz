import weakref

def weak_ref(obj, callback=None):
    if callback:
        return weakref.ref(obj, callback)
    else:
        return weakref.ref(obj)
