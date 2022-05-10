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

while True:
    latefin.__getattribute__('ref')()


# To reproduce this, this code could be run in a subprocess.
# I couldn't reproduce it with gc.disable() and gc.collect(),
# but maybe I'm doing it wrong.
#
# We need the subclassing of tuple for the __del__ to run
# (the weakref is to break the cyclic reference).
# We need the WeakMethod to be created before the class
# (maybe because after creation, the class becomes immortal?)
# We need the getattr on latefin to break the cyclic ref
# and trigger the __del__.
# We need the getattr to be in a loop because otherwise the
# cyclic ref is too short-lived to be detected.
#
# Martin: I don't see why you need a cyclic reference here.
# Just create a WeakMethod for the tuple class and break the
# reference to the tuple, and call the WeakMethod to trigger
# the __del__ method of the tuple class.  You should be able
# to reproduce it without involving a sub
