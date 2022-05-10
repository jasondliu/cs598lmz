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

# This is a bit of a hack, but it's the easiest way to get an
# instancemethod from a class and a function.  The 'repr' leaves a
# reference to the function in the class dict, which is cleared when the
# instancemethod is deleted.
type.__repr__.__dict__['__doc__'] = LateFin()

# This does a number of things.  It gets an instancemethod (keeping a
# reference to the function), it converts the instancemethod to a
# method, and it converts the method to a function.
latefin.__class__.__del__.im_func.im_self.__class__.__doc__.__doc__

# This should trigger the finalizer.
del latefin
