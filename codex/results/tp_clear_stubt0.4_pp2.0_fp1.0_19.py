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

del latefin

# The above code creates a weakref to a function object, which is
# then deleted.  The function object is part of a cycle, which
# includes a __del__ method that creates a weakref to the function
# object.  The __del__ method is called when the cycle is collected,
# which creates the weakref.  The function object is then deleted,
# calling the weakref callback, which sets a global var to the
# function object.  When the weakref is then deleted, the function
# object is also deleted, calling the __del__ method, which creates
# another weakref to the function object.  The cycle is then
# collected again, calling the __del__ method, which creates another
# weakref to the function object.  The function object is then
# deleted, calling the weakref callback, which sets the global var to
# the function object.  When the weakref is then deleted, the
# function object is also deleted, calling the __del__ method, which
# creates another weakref to the function object.  The cycle is then
# collected again
