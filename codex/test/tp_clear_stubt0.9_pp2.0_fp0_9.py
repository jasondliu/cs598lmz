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
gc.collect()
gc.collect()
gc.collect()

# If the cyclic gc problem works, this will crash
# the first time it's called.

# This could, accidentally, free the method too late. 
# To prevent this from happening the reference to func 
# is stored in a global variable. This global variable
# could itself be garbage-collected too late so that a 
# new call to the garbage collector is necessary to prevent
# a crash.

class AlmostNothing:
    def thing(self):
        """It's almost like nothing."""

def test():
    x = AlmostNothing()
    x.thing()

for i in range(500):
    test()
