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

# Get rid of everything else
gc.collect()

# Now the only thing left is the cyclic reference.
# The del-method of LateFin will be called and will
# assign a reference to the function to the 'ref'
# attribute of the LateFin instance.  The function
# __module__ attribute is a reference to the LateFin
# instance and will be the last reference to the
# LateFin instance.  The del-method of Cyclic will
# then be called and will assign a reference to the
# cyclic tuple to the 'ref' attribute of the LateFin
# instance, making the cyclic tuple reachable again.
# At this point, the cyclic garbage collector
# should recognize the cyclic reference and break
# it.

# This test is sensitive to the order in which the
# objects are destroyed.  The key is that the
# LateFin instance must be destroyed before the
# cyclic tuple.  This is why we have the __slots__
# attribute in LateFin.  If the LateFin instance
# were to have a __dict__, then it would be destroyed
# after the
