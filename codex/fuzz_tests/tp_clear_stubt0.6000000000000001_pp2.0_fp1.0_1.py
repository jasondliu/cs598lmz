import gc, weakref

class LateFin:
    __slots__ = ('ref',)
    def __del__(self):
        global func
        func = self.ref()

class Cyclic(tuple):
    __slots__ = ()
    def __del__(self):
        self[1].ref = weakref.ref(self[0])
        global latefin
        del latefin

latefin = LateFin()
func = lambda: None
cyc = tuple.__new__(Cyclic, (func, latefin))

func.__module__ = cyc
del func, cyc

gc.collect()

# Test for bug #1715150:  weakref callbacks on extension type instances
# that have a __del__ method could crash in debug builds.  This is because
# the tp_del slot wasn't checked.

import weakref

class C(object):
    def __init__(self, callback):
        self.callback = callback

    def __del__(self):
        self.callback(self)

def callback(obj):
    pass

x = C(callback)
w = weakref.ref(x)

del x
gc.collect()

# Test for SF bug #503742:  weakref callbacks on old-style instances
# could crash if they resurrected the instance.  This is because the
# instance might be in the middle of being torn down, and refcounting
# it could invoke arbitrary C code with the assumption that the object
# is still mostly intact.

import weakref

class C:
    def __del__(self):
        self.foo = 42

x = C()
w = weakref.
