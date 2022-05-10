import weakref
# Test weakref.ref(weakref.ref(None))
#
# This should not cause a crash.

import weakref

def f():
    return weakref.ref(weakref.ref(None))

