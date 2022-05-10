import gc, weakref
lastref = None

def _fork():
    global lastref
    for i in range(5):
        c = weakref.ref(allocate())
        if lastref is not None and lastref() is not None:
            return False
        lastref = c
    return True

