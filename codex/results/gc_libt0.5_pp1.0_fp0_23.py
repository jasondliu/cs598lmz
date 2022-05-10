import gc, weakref, sys
import threading

#
# These are the tests that run in a separate thread
#

def run_tests():
    import time
    import _weakref
    import gc

    for i in range(10):
        x = [{}]
        x[0]["foo"] = x
        y = _weakref.ref(x)
        while y() is not None:
            time.sleep(0.01)
            gc.collect()
        del x, y

    for i in range(10):
        x = [{}]
        y = weakref.ref(x)
        while y() is not None:
            time.sleep(0.01)
            gc.collect()
        del x, y

    for i in range(10):
        x = [{}]
        y = weakref.ref(x)
        while y() is not None:
            time.sleep(0.01)
            gc.collect()
        del x, y

    for i in range(10):
        x = [{}]

